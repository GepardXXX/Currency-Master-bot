from aiogram.types import CallbackQuery
from aiogram.dispatcher import FSMContext
from bot.texts import rate_texts
from bot.keyboards import back_button
from utils.currency_converter import CurrencyConverter


# Обработчик запросов на отображение текущего курса выбранной валюты
async def handle_currency_button(call: CallbackQuery, state: FSMContext):
    currency = call.data 
    rate = getattr(CurrencyConverter(), f"get_{currency}_rate")()
    rate_text = rate_texts[currency].format(rate=rate)
    await call.bot.edit_message_text(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        text=rate_text,
        reply_markup=back_button()
    )
