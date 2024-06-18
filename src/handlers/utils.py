from aiogram import types

import src.keyboards as kb


async def send_menu(message: types.Message):
    await message.answer("Приёмная комиссия КНИТУ-КАИ", reply_markup=kb.main)
