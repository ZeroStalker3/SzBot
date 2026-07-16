import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.client.session.aiohttp import AiohttpSession 
from config import TOKEN, PROXY_URL
from database import init_db
from handlers import start, menu, order

session = AiohttpSession(proxy=PROXY_URL)

bot = Bot(token=TOKEN, session=session)
dp = Dispatcher()

dp.include_router(start.router)
dp.include_router(menu.router)
dp.include_router(order.router)

async def main():
    logging.basicConfig(level=logging.INFO) 
    init_db()  
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logging.error("Бот остановлен!")
