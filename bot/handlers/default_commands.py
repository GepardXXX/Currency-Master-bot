from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

from keyboards import create_currency_conversion_keyboard, create_currency_keyboard
from text_messages import (
    calculate_message,
    currency_message,
    help_message,
    start_message,
)

router = Router()


@router.message(CommandStart())
async def start_cmd(message: Message):
    username = message.from_user.username or "Незнакомец"

    await message.answer(start_message.format(username))


@router.message(Command("help"))
async def help_cmd(message: Message):
    await message.answer(help_message)


@router.message(Command("course"))
async def course_cmd(message: Message):
    await message.answer(currency_message, reply_markup=create_currency_keyboard())


@router.message(Command("convert"))
async def convert_cmd(message: Message):
    await message.answer(
        calculate_message, reply_markup=create_currency_conversion_keyboard()
    )
