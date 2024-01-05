from aiogram import Router, F, Bot
from aiogram.types import Message

from config import CHAT_ID_OWNER

router = Router()

@router.message(F.text.lower().in_(["хай", "хелоу", "привет"]))
async def greetings(message: Message):
    await message.reply("Привееееть!\nЧто рассказать?")
    await message.answer("Выберите кнопку из представленных ниже")


@router.message()
async def echo(message: Message, bot: Bot):
    print( message )
    if message.text:
        msg = message.text.lower()

        if msg == 'место регистрации':
            text = 'улица белых Роз, в красивом домике'
            await message.answer(f"Регистрация пройдёт по адресу:\n{text}")
        elif msg == 'место праздника':
            text = 'улица красных Роз, направо в красивый домик'
            await message.answer(f"Праздник пройдёт по адресу:\n{text}")
        elif msg == "программа праздника":
            text = 'тамада весёлый и конкурсы интересные'
            await message.answer(f"программа праздника:\n{text}")

    if message.contact:
        chat_id = CHAT_ID_OWNER
        print(message.contact)
        await bot.send_message(chat_id, f"Через бота оставлен контакт: {message.contact.first_name} "
                                        f"{message.contact.last_name}, {message.contact.phone_number}" )
