from aiogram.types import CallbackQuery
from aiogram.utils.exceptions import MessageNotModified
from aiogram.dispatcher import FSMContext
from bot.keyboards import back_button, select_amount_keyboard
from bot.states import ConversionStates
from bot.texts import conversion_success_message, entered_amount
from utils.currency_converter import CurrencyConverter


async def handle_amount_selection(call: CallbackQuery, state: FSMContext):
    new_value = call.data
    async with state.proxy() as data:
        
        # Обработка действий пользователя
        if new_value == 'clear_one':
            data['amount'] = data['amount'][:-1]
        elif new_value == 'clear_all':
            data['amount'] = ''
        elif new_value == 'done':
            amount = data['amount']

            if amount:
                currency_from = data['currency_from']
                currency_to = data['currency_to']
                currency_converter = CurrencyConverter()

                # Определение метода для получения курса валюты
                rate_method = f"get_{currency_to}_rate" if currency_from == 'rub' else f"get_{currency_from}_rate"
                rate = getattr(currency_converter, rate_method)()
                multiplication = currency_from != 'rub'

                # Вычисление результата конвертации и его отправка пользователю
                result = currency_converter.convert(amount, rate, multiplication)
                await call.message.edit_text(
                    conversion_success_message.format(result=result), 
                    reply_markup=back_button(), 
                    parse_mode="Markdown"
                )
                await ConversionStates.FINISH_RESULT.set()
                return 
            
        else:
            data['amount'] = data.get('amount', '') + new_value 

    try:
        # Обновление сообщения с введенной суммой валюты
        amount = data['amount']
        await call.message.edit_text(
            entered_amount.format(amount=amount), 
            reply_markup=select_amount_keyboard(), 
            parse_mode="Markdown"
        )
    except MessageNotModified:
        pass