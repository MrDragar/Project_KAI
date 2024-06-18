from aiogram import types
from aiogram.dispatcher.router import Router
from aiogram.fsm.context import FSMContext

from src.states import SendFeedbackState
from src.config import ADMINS_ID

router = Router()


@router.message(SendFeedbackState.step1)
async def answer(message: types.Message, state: FSMContext):
    for admin_id in ADMINS_ID:
        await message.bot.send_message(admin_id, message.text)
    await state.clear()
