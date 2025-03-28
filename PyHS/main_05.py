"""Бот пиццерии"""

import asyncio
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from dotenv import find_dotenv, load_dotenv
from handlers.user_private import user_private_router


load_dotenv(find_dotenv())
ALOWED_UPDATES = ['message, edited_message']


bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher()
dp.include_routers(user_private_router)




    
 
async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=ALOWED_UPDATES)


if __name__ == "__main__":
    asyncio.run(main())









