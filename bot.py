import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.client.session.aiohttp import AiohttpSession  # Добавляем этот импорт
from config import TOKEN
from database import init_db
from handlers import start, menu, order

# Настраиваем прокси. 1080 — это порт твоего контейнера xray-client
session = AiohttpSession(proxy="socks5://127.0.0.1:1080")

# Инициализация бота с использованием сессии
bot = Bot(token=TOKEN, session=session)
dp = Dispatcher()

# Подключаем роутеры
dp.include_router(start.router)
dp.include_router(menu.router)
dp.include_router(order.router)

async def main():
    logging.basicConfig(level=logging.INFO) # Полезно видеть логи, если что-то пойдет не так
    init_db()  
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logging.error("Бот остановлен!")
