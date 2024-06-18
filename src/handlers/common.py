from aiogram.dispatcher.router import Router
from aiogram import types, F
from aiogram.filters import CommandStart, Command

from .utils import send_menu

router = Router()


@router.message(CommandStart())
async def cmd(message: types.Message):
    await send_menu(message)


@router.message(F.text == "🔼 Вернуться в меню 🔼")
@router.message(Command("cancel"))
async def back_to_main_menu(message: types.Message):
    await send_menu(message)


@router.message()
async def entry_point(message: types.Message):
    await message.answer('❌ Я тебя не понимаю ❌')
