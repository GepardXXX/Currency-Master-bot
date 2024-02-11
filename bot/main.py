import asyncio

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from handlers import setup_routers
from settings import config
from utils.ui_commands import setup_bot_commands


async def main():
    storage = MemoryStorage()
    bot = Bot(config.bot_token.get_secret_value(), parse_mode="HTML")
    dp = Dispatcher(storage=storage)

    routers = setup_routers()
    dp.include_routers(routers)

    await setup_bot_commands(bot)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
