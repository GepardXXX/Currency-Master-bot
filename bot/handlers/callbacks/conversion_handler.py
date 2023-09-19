from aiogram.types import CallbackQuery
from aiogram.dispatcher import FSMContext
from bot.states import ConversionStates
from bot.texts import select_amount_message
from bot.keyboards import select_amount_keyboard


# Обработчик запросов на выбор валюты для конвертации
async def handle_conversion_query(call: CallbackQuery, state: FSMContext):
    conversion_data = call.data
    currency_from, currency_to = conversion_data.split('_to_')

    async with state.proxy() as data:
        data['currency_from'] = currency_from
        data['currency_to'] = currency_to
        data['amount'] = ''
        
    await call.message.edit_text(
        select_amount_message,
        reply_markup=select_amount_keyboard()
    )
    await ConversionStates.INPUT_AMOUNT.set()
    

