from aiogram import types, F
from aiogram.dispatcher.router import Router
from aiogram.fsm.context import FSMContext

import src.keyboards as kb
from src.states import SendFeedbackState
import src.reply as sms

router = Router()


@router.message(F.text == "📞 Контакты 📞")
async def cmd_contact(message: types.Message):
    await message.answer(sms.contact_info, reply_markup=kb.contact_kb)


@router.message(F.text == "Об Университете")
async def cmd_info(message: types.Message):
    await message.answer(sms.info_univer)


@router.message(F.text == "🎓 Направления обучения 🎓")
async def cmd_napr(message: types.Message):
    await message.answer("КАИ - пуп земли!", reply_markup=kb.napravl_oboch)


@router.message(F.text == "🕺 Студенческая жизнь 🕺")
async def cmd_stud(message: types.Message):
    await message.answer(sms.stud_life_sms, reply_markup=kb.stud_life)


@router.message(F.text == "🕺 Обратная связь 🕺")
async def answer(message: types.Message, state: FSMContext):
    await message.answer('Напишите ваше обращение в поддержку')
    await state.set_state(SendFeedbackState.step1)
