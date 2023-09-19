from aiogram.types import Message
from bot.texts import help_message


# Отправляет пользователю сообщение со справкой
async def send_help(message: Message):
    await message.answer(help_message, parse_mode="Markdown")