from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def setup_bot_commands(bot: Bot):
    commands = [
        BotCommand(
            command="course",
            description="Получить текущий курс валют"
        ),
        BotCommand(
            command="convert",
            description="Конвертировать из одной валюты в другую"
        ),
        BotCommand(
            command="help",
            description="Справка"
        )
    ]

    await bot.set_my_commands(commands=commands, scope=BotCommandScopeDefault())