



from aiogram import Bot, Router, types
from aiogram.filters import Command

user_private_router = Router()

@user_private_router.message(Command('start'))
async def start(message: types.Message):
    await message.answer('Привет, я  вирутальный помощник')


@user_private_router.message(Command('menu'))
async def echo(message: types.Message, bot:Bot):
    """Эхо"""
    await message.answer('Вот меню:')