from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


# Клавиатура для выбора валюты
def currency_selection_keyboard():
    return InlineKeyboardMarkup(row_width=3).row(
        InlineKeyboardButton(text='USD', callback_data='usd'),
        InlineKeyboardButton(text='EUR', callback_data='eur'),
        InlineKeyboardButton(text='KZT', callback_data='kzt')
    ).row(
        InlineKeyboardButton(text='CNY', callback_data='cny'),
        InlineKeyboardButton(text='UAH', callback_data='uah')
    )