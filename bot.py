import asyncio
import logging
from aiogram import Bot, Dispatcher
from config import TOKEN
from database import init_db
from handlers import start, menu, order

# Инициализация бота
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Подключаем роутеры
dp.include_router(start.router)
dp.include_router(menu.router)
dp.include_router(order.router)

async def main():
    init_db()  # Создаём БД при старте
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
