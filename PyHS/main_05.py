"""Бот пиццерии"""

import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command





bot = Bot(token="7672525355:AAE-TEINCA5rdlFbxIkXvHJvdri15lfY6zg")
dp = Dispatcher()


@dp.message(Command('start'))
async def start(message: types.Message):
    await message.answer('Hello')


@dp.message()
async def echo(message: types.Message):
    """Эхо"""
    text = message.text
    if text in ["Привет", "привет", "hi", "hello"]:
        await message.answer('И тебе привет')
    elif text in ["Пока", "пока", "пакеда", "До свидания"]:
        await message.answer("И тебе пока")
    else:
        await message.answer(message.text)
    
    



async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())









