from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from keyboards import create_back_keyboard
from states import CurrencyStates
from text_messages import rate_texts
from utils.currency_scraper import CurrencyScraper

router = Router()
currencies = ["usd", "eur", "kzt", "cny", "uah"]


@router.callback_query(F.data.in_(currencies))
async def show_currency_rate(call: CallbackQuery, state: FSMContext):
    '''
    Показывает текущий курс выбранной валюты.
    '''
    currency = call.data
    rate = getattr(CurrencyScraper(), f"get_{currency}_rate")()
    rate_text = rate_texts[currency].format(rate)

    await call.message.edit_text(
        text=rate_text,
        reply_markup=create_back_keyboard(),
    )
    await state.set_state(CurrencyStates.showing_currency_rate)
