from aiogram.filters.state import State, StatesGroup


class CurrencyStates(StatesGroup):
    showing_currency_rate = State()
    entering_amount = State()
    conversion_completed = State()