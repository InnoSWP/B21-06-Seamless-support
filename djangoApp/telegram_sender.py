from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils import executor
from aiogram import Bot, Dispatcher
from core.Database.database import GoogleSheets
import config
import os

API_TOKEN = '5566247924:AAE5b_fEMsbRyuNZrsC3O33zkqEXwmoESJA'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
gs = GoogleSheets()


def watch_file_update(path):
    timestamp = os.stat(path).st_mtime
    while 1:
        if timestamp != os.stat(path).st_mtime:
            timestamp = os.stat(path).st_mtime
            print('Файл изменён!')
            return 1


async def somefunc():
    button_hi = KeyboardButton('Получить вопрос')

    greet_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    greet_kb.add(button_hi)

    while 1:
        if watch_file_update("file.txt"):
            mess = open("file.txt", "r").read().split('\n')
            num_of_q = gs.add_message_to_queue(user_id=mess[0], text=mess[1])
            await bot.send_message(config.CHAT_ID, "Новый вопрос. Всего вопросов - " + str(num_of_q), reply_markup=greet_kb)


if __name__ == '__main__':
    executor.start(dp, somefunc())
