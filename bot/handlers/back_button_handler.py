from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from keyboards import (
    create_amount_input_keyboard,
    create_currency_conversion_keyboard,
    create_currency_keyboard,
)
from states import CurrencyStates
from text_messages import calculate_message, currency_message, select_amount_message

router = Router()


@router.callback_query(F.data == "back_button")
async def handle_back_button(call: CallbackQuery, state: FSMContext):
    currency_state = await state.get_state()

    match currency_state:
        case CurrencyStates.showing_currency_rate:
            await call.message.edit_text(
                text=currency_message,
                reply_markup=create_currency_keyboard(),
            )
            await state.clear()

        case CurrencyStates.entering_amount:
            await call.message.edit_text(
                text=calculate_message,
                reply_markup=create_currency_conversion_keyboard(),
            )
            await state.clear()

        case CurrencyStates.conversion_completed:
            await call.message.edit_text(
                text=select_amount_message,
                reply_markup=create_amount_input_keyboard(),
            )
            await state.update_data({"amount": ""})
            await state.set_state(CurrencyStates.entering_amount)
