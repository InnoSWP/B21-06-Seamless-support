import asyncio
import logging
import os
from random import randint
from datetime import datetime, timedelta
from aiogram.utils.callback_data import CallbackData
from aiogram import Bot, Dispatcher, executor, types, filters
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton, Update
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoApp.settings')
import django
django.setup()
from core.views import add_answers

import config

bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

@dp.message_handler(commands='get_questions')
async def cmd_random(message: types.Message):
    f = open("file.txt", "r")
    USER_NAME = f.readline()
    USER_QUESTION = f.readline()


    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Принять ✅", callback_data="accept"))
    keyboard.add(types.InlineKeyboardButton(text="Отклонить ❌", callback_data="decline"))
    await message.answer("Имя: " + USER_NAME + "\nВопрос: " + USER_QUESTION, reply_markup=keyboard)
    f.close()


@dp.message_handler()
async def get_answers(message: types.Message):
    f = open('answer.txt', 'a')
    f.write(str(message.from_user.id) + ':')
    f.write(message.text+'\n')
    f.close()
    add_answers(message=message.text, vol_id=str(message.from_user.id))


@dp.callback_query_handler(text="accept")
async def send_random_value(call: types.CallbackQuery):
    f = open("answer.txt", "r")
    USER_NAME = f.readline()
    USER_QUESTION = f.readline()

    volunteer_id = call.from_user.id
    volunteer_name = call.from_user.first_name


    await call.message.answer("Вопрос был принят " + volunteer_name)
    await bot.send_message(volunteer_id, "Вопрос от " + USER_NAME + "\n" + USER_QUESTION)

    f.close()

    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Начать помогать", callback_data="start"))
    keyboard.add(types.InlineKeyboardButton(text="Закончить помогать", callback_data="finish"))
    await bot.send_message(volunteer_id, "Выберите действие", reply_markup=keyboard)

    @dp.callback_query_handler(text="start")
    async def start_help(call: types.CallbackQuery):
        await bot.send_message(volunteer_id, "Напишите решение проблемы")

    @dp.callback_query_handler(text="finish")
    async def finish_help(call: types.CallbackQuery):
        await bot.send_message(volunteer_id, "Ваш ответ отправлен\nСпасибо!")

        file_answer = open("../answer.txt", "a")

        file_answer.write()

        file_answer.write("answer_help")
        file_answer.close()
        await call.message.delete()

        # TODO: тут нужно прописать как происходит отправка ответа пользователю/в бд

    await call.message.delete()


@dp.callback_query_handler(text="decline")
async def send_random_value(call: types.CallbackQuery):
    volunteer_name = call.from_user.first_name
    await call.message.answer("Вопрос был отклонен " + volunteer_name)


executor.start_polling(dp, skip_updates=True)