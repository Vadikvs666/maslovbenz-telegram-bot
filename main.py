import logging
import os

import aiogram
from aiogram import types
from dotenv import load_dotenv
from pathlib import Path

dotenv_path = Path('.env')
load_dotenv(dotenv_path=dotenv_path)
API_TOKEN = os.getenv('API_TOKEN')

logging.basicConfig(level=logging.INFO)

bot = aiogram.Bot(API_TOKEN)
dp = aiogram.Dispatcher(bot)

users_data = dict()


@dp.message_handler(commands=['start'])
async def start_handler(message: aiogram.types.Message):
    logging.info(" start bot")
    await message.reply("Привет!\nЯ бот который поможет расчитать сколько масла нужно добавлять в бензин\nдля "
                        "2х-тактных моторов."
                        "Напишите сколько у вас литров бензина")


@dp.message_handler(commands=['help'])
async def help_handler(message: aiogram.types.Message):
    logging.info(" get  help")
    await message.reply("Напишите боту сколько у вас литров бензина")


@dp.message_handler()
async def message_handler(message: aiogram.types.Message):
    logging.info("send liters - " + message.text)
    try:
        liters = int(message.text)
        users_data[message.chat.id] = liters
        keyboard_markup = types.InlineKeyboardMarkup(row_width=3)
        text_and_data = (
            ('1/25', '25'),
            ('1/50', '50'),
            ('1/100', '100'),
        )
        # in real life for the callback_data the callback data factory should be used
        # here the raw string is used for the simplicity
        row_btns = (types.InlineKeyboardButton(text, callback_data=data) for text, data in text_and_data)
        keyboard_markup.row(*row_btns)
        await message.reply("Выберите пропорцию: ", reply_markup=keyboard_markup)
    except Exception as e:
        logging.info(f'Invalid input from user')
        await message.reply("Напишите боту сколько у вас литров бензина")


@dp.callback_query_handler(text='50')  # if cb.data == 'no'
@dp.callback_query_handler(text='100')  # if cb.data == 'yes'
@dp.callback_query_handler(text='25')  # if cb.data == 'yes'
async def inline_kb_answer_callback_handler(query: types.CallbackQuery):
    answer_data = query.data
    # always answer callback queries, even if you have nothing to say
    await query.answer(f' Вы выбрали - 1/{answer_data!r}')
    logging.info(f' Selected -  {answer_data!r}')

    try:
        prop = int(answer_data)
        liters = int(users_data[query.from_user.id])
        res = int(liters/prop*1000);
        text = f'Вам необходимо {res} миллилитров масла'
    except Exception as e:
        logging.info(f'Invalid input from user')
        text = f'Напишите боту сколько у вас литров бензина!'

    await bot.send_message(query.from_user.id, text)


aiogram.executor.start_polling(dp, skip_updates=True)
