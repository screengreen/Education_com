import asyncio
from botdb import BotDB
from aiogram import Bot, Dispatcher, executor
from config import BOT_TOKEN
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

loop = asyncio.get_event_loop()
bot = Bot(BOT_TOKEN, parse_mode='HTML')

dp = Dispatcher(bot, storage=storage, loop=loop)
BotDB1 = BotDB('bot.db')


async def on_startup(_):
    print('Бот запущен')


if __name__ == '__main__':
    from handlers import dp
    executor.start_polling(dp, on_startup=on_startup)