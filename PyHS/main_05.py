"""Бот пиццерии"""
import asyncio
import os
from dotenv import find_dotenv, load_dotenv

from aiogram import Bot, Dispatcher, Router, types
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import Command


from middlewares.db import CounterMiddleware
from common.bot_cmds_list import private

from handlers.user_private import user_private_router
from handlers.user_group import user_group_router
from handlers.admin_private import admin_router


load_dotenv(find_dotenv())
ALOWED_UPDATES = ['message, edited_message']


bot = Bot(token=os.getenv('TOKEN'), default=DefaultBotProperties(parse_mode=ParseMode.HTML))
bot.my_admins_list = []
dp = Dispatcher()


dp.include_routers(user_private_router)
dp.include_routers(user_group_router)
dp.include_router(admin_router)

admin_router.message.outer_middleware(CounterMiddleware())


    
 
async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    # await bot.delete_my_commands(scope=types.BotCommandScopeAllPrivateChats()) если нужно изменить кнопки меню
    await bot.set_my_commands(commands=private, scope=types.BotCommandScopeAllPrivateChats())
    await dp.start_polling(bot, allowed_updates=ALOWED_UPDATES)


if __name__ == "__main__":
    asyncio.run(main())









