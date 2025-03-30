



from aiogram import F, Bot, Router, types
from aiogram.filters import Command, or_f

user_private_router = Router()

@user_private_router.message(Command('start'))
async def start(message: types.Message):
    await message.answer('Привет, я  вирутальный помощник')


@user_private_router.message(or_f(Command('menu'), (F.text.lower() == 'меню'))) 
async def menu(message: types.Message):
    """Эхо"""
    await message.answer('Вот меню:')


@user_private_router.message(F.text.lower() == 'о нас')
@user_private_router.message(Command('about'))
async def about(message: types.Message):
    await message.answer('О нас:')


@user_private_router.message(F.text.lower() == 'варианты оплаты')
@user_private_router.message(Command('payment'))
async def payment(message: types.Message):
    await message.answer('Варианты оплаты:')


@user_private_router.message(F.text.lower().contains('доставк'))
@user_private_router.message(Command('shipping'))
async def shipping(message: types.Message):
    await message.answer('Варианты доставки:')


# @user_private_router.message(F.text.lower().contains('доставк'))
# async def shipping(message: types.Message):
#     await message.answer('Это магический фильтр')


