from aiogram import Dispatcher
from .handlers import commands, callbacks
from bot.states import ConversionStates


def setup(dp: Dispatcher):
    # Регистрация обработчиков команд
    register_command_handlers(dp)

    # Регистрация обработчиков кнопок с валютами
    register_currency_button_handlers(dp)

    # Регистрация обработчиков конвертации
    register_conversion_handlers(dp)

    # Регистрация обработчиков для ввода суммы
    register_amount_input_handlers(dp)

    # Регистрация обработчиков кнопки "назад"
    register_back_button_handlers(dp)

def register_command_handlers(dp):
    dp.register_message_handler(
        commands.welcome,
        commands=['start']
    )
    dp.register_message_handler(
        commands.start_conversion,
        commands=['convert']
    )
    dp.register_message_handler(
        commands.send_help,
        commands=['help']
    )
    dp.register_message_handler(
        commands.send_course,
        commands=['course'],
        state='*'
    )

def register_currency_button_handlers(dp):
    dp.register_callback_query_handler(
        callbacks.handle_currency_button,
        text=['usd', 'eur', 'kzt', 'cny', 'uah']
    )

def register_conversion_handlers(dp):
    dp.register_callback_query_handler(
        callbacks.handle_conversion_query,
        text=[
            'rub_to_usd', 'usd_to_rub', 'rub_to_eur', 'eur_to_rub',
            'rub_to_kzt', 'kzt_to_rub', 'rub_to_cny', 'cny_to_rub',
            'rub_to_uah', 'uah_to_rub'
        ],
        state=ConversionStates.SELECT_CONVERSION
    )

def register_amount_input_handlers(dp):
    dp.register_callback_query_handler(
        callbacks.handle_amount_selection,
        text=[
            "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ".", 'clear_one', 'clear_all', 'done'
        ],
        state=ConversionStates.INPUT_AMOUNT
    )

def register_back_button_handlers(dp):
    dp.register_callback_query_handler(
        callbacks.handle_back_button_1,
        text=['back'],
        state=ConversionStates.INPUT_AMOUNT
    )
    dp.register_callback_query_handler(
        callbacks.handle_back_button_2,
        text=['back'],
        state=ConversionStates.FINISH_RESULT
    )
    dp.register_callback_query_handler(
        callbacks.handle_back_button,
        text=['back']
    )
