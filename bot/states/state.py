from aiogram.dispatcher.filters.state import State, StatesGroup


class ConversionStates(StatesGroup):
    SELECT_CONVERSION = State()  # Состояние выбора конверсии валют
    INPUT_AMOUNT = State()  # Состояние ввода суммы
    FINISH_RESULT = State()  # Состояние завершения конверсии и вывода результата
