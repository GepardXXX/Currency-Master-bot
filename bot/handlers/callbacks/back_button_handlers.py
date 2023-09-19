from aiogram.types import CallbackQuery
from aiogram.dispatcher import FSMContext
from bot.texts import currency_message, select_amount_message
from bot.states import ConversionStates
from bot.keyboards import currency_selection_keyboard, conversion_selection_keyboard, select_amount_keyboard


# Обработчик кнопки "Назад" при выборе валюты
async def handle_back_button(call: CallbackQuery):
    await call.bot.edit_message_text(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        text=currency_message,
        reply_markup=currency_selection_keyboard()
    )

# Обработчик кнопки "Назад" при выборе преобразования
async def handle_back_button_1(call: CallbackQuery, state: FSMContext):
    await call.bot.edit_message_text(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        text=currency_message,
        reply_markup=conversion_selection_keyboard()
    )
    await ConversionStates.SELECT_CONVERSION.set()

# Обработчик кнопки "Назад" при выборе суммы
async def handle_back_button_2(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['amount'] = ''

    await call.bot.edit_message_text(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        text=select_amount_message,
        reply_markup=select_amount_keyboard()
    )
    await ConversionStates.INPUT_AMOUNT.set()