from aiogram import F, Bot, Router, types

from aiogram.filters import Command, or_f
from aiogram.utils.formatting import as_list, as_marked_section, Bold
from filters.chat_types import ChatTypesFilter
from keyboards import reply

user_private_router = Router()
user_private_router.message.filter(ChatTypesFilter(['private']))

@user_private_router.message(Command('start'))
async def start(message: types.Message):
    await message.answer('Привет, я  вирутальный помощник', 
                         reply_markup=reply.start_kb3.as_markup(
                             resize_keyboard=True,
                             input_field_placeholder ='Что вас инетересует?')

    )


@user_private_router.message(or_f(Command('menu'), (F.text.lower() == 'меню'))) 
async def menu(message: types.Message):
    """Эхо"""
    await message.answer('Вот меню:', reply_markup=reply.del_kbd)


@user_private_router.message(F.text.lower() == 'о нас')
@user_private_router.message(Command('about'))
async def about(message: types.Message):
    await message.answer('О нас:')


@user_private_router.message(F.text.lower() == 'варианты оплаты')
@user_private_router.message(Command('payment'))
async def payment(message: types.Message):

    text = as_marked_section(
        Bold("Варианты оплаты"),
        "Картой в боте",
        "При получении карта/кеш",
        "В заведении",
        marker='✅'
    )
    await message.answer(text.as_html())


@user_private_router.message(F.text.lower().contains('доставк'))
@user_private_router.message(Command('shipping'))
async def shipping(message: types.Message):
    text = as_list(
        as_marked_section(
        Bold("Варианты доставки"),
        "Курьер",
        "Самовынос",
        "Покушаю у вас",
        marker='✅'
    ),
    as_marked_section(
        Bold("Нельзя"),
        'Почта',
        'Голуби',
        marker='❌'
         
     ),
    sep='\n------------------------------\n'
    )
    await message.answer(text.as_html())


# @user_private_router.message(F.text.lower().contains('доставк'))
# async def shipping(message: types.Message):
#     await message.answer('Это магический фильтр')


@user_private_router.message(F.contact)
async def get_contact(message: types.Message):
    await message.answer(f'номер получен')
    await message.answer(str(message.contact))


@user_private_router.message(F.location)
async def get_location(message: types.Message):
    await message.answer(f'локация получена')
    await message.answer(str(message.location))