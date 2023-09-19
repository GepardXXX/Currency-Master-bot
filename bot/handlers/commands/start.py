from aiogram.types import Message
from bot.texts import start_message


# Приветственное сообщение
async def welcome(message: Message):
    user_name = message.from_user.username or '_User_'
    await message.answer(
        start_message.format(user_name=user_name), parse_mode= "Markdown")



        