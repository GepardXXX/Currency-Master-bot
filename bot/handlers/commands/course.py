from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from bot.texts import currency_message
from bot.keyboards import currency_selection_keyboard
    

# Обработчик команды "course"(отправка курса валют пользователю)
async def send_course(message: Message, state: FSMContext):
    await message.answer(
        currency_message, reply_markup=currency_selection_keyboard()
    )
    await state.finish()