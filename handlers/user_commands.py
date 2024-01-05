from aiogram import Router, Bot
from aiogram.types import Message
from aiogram.filters import Command, CommandStart, CommandObject

from keyboards import reply

router = Router()

@router.message(CommandStart())
async def handle_start(message: Message):
    text =  f"Привет, <b>{message.from_user.first_name}</b>!\n"
    await message.answer(text=text, reply_markup=reply.main)

