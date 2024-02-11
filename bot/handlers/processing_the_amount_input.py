from typing import Any, Dict

from aiogram import Router
from aiogram.exceptions import TelegramBadRequest
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from keyboards import create_amount_input_keyboard, create_back_keyboard
from states import CurrencyStates
from text_messages import conversion_success_message, entered_amount_message
from utils.currency_scraper import CurrencyScraper

router = Router()


@router.callback_query(CurrencyStates.entering_amount)
async def handle_amount_input(call: CallbackQuery, state: FSMContext):
    """
    Обработка введенной пользователем суммы.
    """
    new_value = call.data
    data = await state.get_data()

    # Обработка действий пользователя
    match new_value:
        case "clear_one":
            data["amount"] = data["amount"][:-1]
        case "clear_all":
            data["amount"] = ""
        case "done":
            amount = data["amount"]

            if amount:
                await process_conversion(data, call)
                await state.set_state(CurrencyStates.conversion_completed)
                return
        case _:
            data["amount"] += new_value

    # Обновление сообщения с введенной суммой валюты
    try:
        amount = data["amount"]
        await call.message.edit_text(
            text=entered_amount_message.format(amount),
            reply_markup=create_amount_input_keyboard(),
        )
        await state.set_data(data)
    except TelegramBadRequest:
        pass


async def process_conversion(data: Dict[str, Any], call: CallbackQuery):
    amount = data["amount"] if data["amount"] != "." else "0"
    currency_from = data["currency_from"]
    currency_to = data["currency_to"]
    cs = CurrencyScraper()

    # Определение метода для получения курса валюты
    rate_method = (
        f"get_{currency_to}_rate"
        if currency_from == "rub"
        else f"get_{currency_from}_rate"
    )
    rate = getattr(cs, rate_method)()
    multiplication = currency_from != "rub"

    # Вычисление результата конвертации и его отправка пользователю
    result = cs.convert(
        currency_1=amount, currency_2=rate, multiplication=multiplication
    )

    await call.message.edit_text(
        text=conversion_success_message.format(result),
        reply_markup=create_back_keyboard(),
    )
