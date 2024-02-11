from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardButton


# Клавиатура для ввода суммы
def create_amount_input_keyboard():
    buttons = [
        [
            InlineKeyboardButton(text="1", callback_data="1"),
            InlineKeyboardButton(text="2", callback_data="2"),
            InlineKeyboardButton(text="3", callback_data="3"),
        ],
        [
            InlineKeyboardButton(text="4", callback_data="4"),
            InlineKeyboardButton(text="5", callback_data="5"),
            InlineKeyboardButton(text="6", callback_data="6"),
        ],
        [
            InlineKeyboardButton(text="7", callback_data="7"),
            InlineKeyboardButton(text="8", callback_data="8"),
            InlineKeyboardButton(text="9", callback_data="9"),
        ],
        [
            InlineKeyboardButton(text=".", callback_data="."),
            InlineKeyboardButton(text="0", callback_data="0"),
            InlineKeyboardButton(text="CE", callback_data="clear_one"),
        ],
        [
            InlineKeyboardButton(text="Назад", callback_data="back_button"),
            InlineKeyboardButton(text="Очистить", callback_data="clear_all"),
        ],
        [InlineKeyboardButton(text="Готово", callback_data="done")],
    ]

    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard

