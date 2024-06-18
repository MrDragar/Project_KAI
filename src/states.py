from aiogram.fsm.state import State, StatesGroup


class SendFeedbackState(StatesGroup):
    step1 = State()


class AnswerFeedbackState(StatesGroup):
    step1 = State()
