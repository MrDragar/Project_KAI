from aiogram.dispatcher.router import Router
from . import common
from . import menu

router = Router()
router.include_router(menu.router)
router.include_router(common.router)

