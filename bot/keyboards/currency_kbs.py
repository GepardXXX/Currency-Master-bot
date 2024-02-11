from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton


# Клавиатура для выбора валюты
def create_currency_keyboard():
    builder = InlineKeyboardBuilder()
    currencies = ["USD", "EUR", "KZT", "CNY", "UAH"]

    for currency in currencies:
        builder.add(InlineKeyboardButton(text=currency, callback_data=currency.lower()))

    builder.adjust(3)
    return builder.as_markup()


# Клавиатура для выбора конверсии валют
def create_currency_conversion_keyboard():
    builder = InlineKeyboardBuilder()
    currencies = [
        "RUB to USD",
        "USD to RUB",
        "RUB to EUR",
        "EUR to RUB",
        "RUB to KZT",
        "KZT to RUB",
        "RUB to CNY",
        "CNY to RUB",
        "RUB to UAH",
        "UAH to RUB",
    ]

    for currency in currencies:
        builder.add(
            InlineKeyboardButton(
                text=currency, callback_data=currency.lower().replace(" ", "_")
            )
        )

    builder.adjust(2)
    return builder.as_markup()
