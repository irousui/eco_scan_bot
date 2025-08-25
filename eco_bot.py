import asyncio 
import logging
import os

from aiogram import Bot,Dispatcher
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

# from config import TOKEN
from dotenv import load_dotenv
from app.handlers import router

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
# bot=Bot(token="TOKEN")
dp=Dispatcher()

async def main():
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO) 
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('EXIT')