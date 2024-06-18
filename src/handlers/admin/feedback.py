from aiogram import types
from aiogram.dispatcher.router import Router
from aiogram.fsm.context import FSMContext

from src.callbacks import FeedbackCallback
from src.states import AnswerFeedbackState

router = Router()


@router.callback_query(FeedbackCallback.filter())
async def answer_to_user(
        callback_query: types.CallbackQuery,
        callback_data: FeedbackCallback,
        state: FSMContext
) -> None:
    await callback_query.message.answer("Напишите ответ пользователю")
    await state.set_state(AnswerFeedbackState.step1)
    await state.update_data(chat_id=callback_data.user_id)


@router.message(AnswerFeedbackState.step1)
async def send_answer(message: types.Message, state: FSMContext) -> None:
    user_chat_id = (await state.get_data())["chat_id"]
    await message.send_copy(chat_id=user_chat_id)
    await state.clear()
