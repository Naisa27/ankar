import asyncio
import logging

from aiogram import Bot, Dispatcher

from handlers import bot_messages, user_commands

from config import BOT_TOKEN



async def main():
    bot = Bot( BOT_TOKEN, parse_mode="HTML")
    dp = Dispatcher()

    dp.include_routers(
        user_commands.router,
        bot_messages.router
    )

    logging.basicConfig(level=logging.INFO)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
