from aiogram.types import Message
from bot.texts import calculate_message
from bot.keyboards import conversion_selection_keyboard
from bot.states import ConversionStates


# Обработчик команды "convert" для начала конвертации
async def start_conversion(message: Message):
    await message.answer(calculate_message, reply_markup=conversion_selection_keyboard())
    await ConversionStates.SELECT_CONVERSION.set()