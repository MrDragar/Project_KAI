from aiogram.dispatcher.router import Router

from . import feedback
from . import common
from . import menu
from . import admin

router = Router()
router.include_router(admin.router)
router.include_router(menu.router)
router.include_router(feedback.router)
router.include_router(common.router)

