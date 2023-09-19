from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


# Клавиатура для выбора конверсии валют
def conversion_selection_keyboard():
    keyboard = InlineKeyboardMarkup(row_width=2)
    buttons = [
        InlineKeyboardButton(text='RUB to USD', callback_data='rub_to_usd'),
        InlineKeyboardButton(text='USD to RUB', callback_data='usd_to_rub'),
        InlineKeyboardButton(text='RUB to EUR', callback_data='rub_to_eur'),
        InlineKeyboardButton(text='EUR to RUB', callback_data='eur_to_rub'),
        InlineKeyboardButton(text='RUB to KZT', callback_data='rub_to_kzt'),
        InlineKeyboardButton(text='KZT to RUB', callback_data='kzt_to_rub'),
        InlineKeyboardButton(text='RUB to CNY', callback_data='rub_to_cny'),
        InlineKeyboardButton(text='CNY to RUB', callback_data='cny_to_rub'),
        InlineKeyboardButton(text='RUB to UAH', callback_data='rub_to_uah'),
        InlineKeyboardButton(text='UAH to RUB', callback_data='uah_to_rub'),
    ]
    keyboard.add(*buttons)
    return keyboard
