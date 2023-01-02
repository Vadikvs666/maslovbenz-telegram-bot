import logging
import os

import aiogram
from dotenv import load_dotenv
from pathlib import Path

dotenv_path = Path('.env')
load_dotenv(dotenv_path=dotenv_path)


API_TOKEN = os.getenv('API_TOKEN')


# Configure logging

logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher

bot = aiogram.Bot(token=API_TOKEN)

dp = aiogram.Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_handler(message: aiogram.types.Message):
    """

    This handler will be called when user sends `/start` or `/help` command

    """
    logging.info(" start bot")
    await message.reply("Привет!\nЯ бот который поможет расчитать сколько масла нужно добавлять в бензин\nдля "
                        "2х-тактных моторов."
                        "Напишите сколько у вас литров бензина")


@dp.message_handler(commands=['help'])
async def help_handler(message: aiogram.types.Message):
    """

    This handler will be called when user sends `/start` or `/help` command

    """
    logging.info(" get  help")
    await message.reply("Напишите боту сколько у вас литров бензина")


@dp.message_handler()
async def text_message(message: aiogram.types.Message):
    logging.info("send liters")
    liters = message.text
    await message.answer(message.text)


aiogram.executor.start_polling(dp, skip_updates=True)
