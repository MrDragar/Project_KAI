from aiogram.filters.callback_data import CallbackData


class FeedbackCallback(CallbackData, prefix="/f"):
    user_id: int
