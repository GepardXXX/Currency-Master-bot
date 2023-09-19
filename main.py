from aiogram import executor
from bot.bot import dp

# Запуск бота
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)


