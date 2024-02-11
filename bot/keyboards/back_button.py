from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardButton


def create_back_keyboard():
    button = [InlineKeyboardButton(text="Назад", callback_data="back_button")]

    keyboard = InlineKeyboardMarkup(inline_keyboard=[button])
    return keyboard
