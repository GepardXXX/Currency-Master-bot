from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


# Кнопка "Назад" для инлайн-клавиатуры
def back_button():
    return InlineKeyboardMarkup().row(
        InlineKeyboardButton(text='Назад', callback_data='back'))