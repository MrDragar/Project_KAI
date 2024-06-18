from aiogram.dispatcher.router import Router

from . import feedback
from src.filters import IsAdmin

router = Router()
router.message.filter(IsAdmin())
router.include_router(feedback.router)
