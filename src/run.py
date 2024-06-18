import asyncio
import logging

from aiogram.types import BotCommand
from aiogram import Bot, Dispatcher

from src.config import API_TOKEN
from src.handlers import router as root_router


# Объект бота
bot = Bot(token=API_TOKEN)

# Диспетчер
dp = Dispatcher()


# Создаем асинхронную функцию
async def set_main_menu(bot: Bot):
    # Создаем список с командами и их описанием для кнопки menu
    main_menu_commands = [
        BotCommand(
            command='/start',
            description='Запуск бота'
        ),
        BotCommand(
            command='/cancel',
            description='Отмена'
        )
    ]
    await bot.set_my_commands(main_menu_commands)


dp.startup.register(set_main_menu)
dp.include_router(root_router)


# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.info('Exit')
