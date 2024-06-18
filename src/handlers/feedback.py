from aiogram import types
from aiogram.dispatcher.router import Router
from aiogram.fsm.context import FSMContext

from src.states import SendFeedbackState
from src.config import ADMINS_ID
from src.keyboards import get_feedback_keyboard

router = Router()


@router.message(SendFeedbackState.step1)
async def send_to_admins(message: types.Message, state: FSMContext):
    for admin_id in ADMINS_ID:
        reply_message = await message.bot.send_message(
            chat_id=admin_id,
            text="Новый запрос в поддержку от {0}".format(message.from_user.full_name)
        )
        await message.copy_to(
            chat_id=admin_id,
            reply_to_message_id=reply_message.message_id,
            reply_markup=get_feedback_keyboard(message.from_user.id)
        )
    await state.clear()
