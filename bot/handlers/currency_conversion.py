from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from keyboards import create_amount_input_keyboard
from states import CurrencyStates
from text_messages import select_amount_message

router = Router()


@router.callback_query(F.data.contains("_to_"))
async def conversion_currency_from_to(call: CallbackQuery, state: FSMContext):
    """
    Обработка валют, которые выбрал пользователь.
    """
    conversion_data = call.data
    currency_from, currency_to = conversion_data.split("_to_")

    await state.update_data(
        currency_from=currency_from, currency_to=currency_to, amount=""
    )
    await call.message.edit_text(
        text=select_amount_message, reply_markup=create_amount_input_keyboard()
    )
    await state.set_state(CurrencyStates.entering_amount)
