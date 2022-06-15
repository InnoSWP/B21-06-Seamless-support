from aiogram.utils import executor
from aiogram import Bot, Dispatcher
import config

API_TOKEN = '5566247924:AAE5b_fEMsbRyuNZrsC3O33zkqEXwmoESJA'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

import os

def watch_file_update(path):
  timestamp = os.stat(path).st_mtime
  while 1:
    if timestamp != os.stat(path).st_mtime:
      timestamp = os.stat(path).st_mtime
      print('Файл изменён!')
      return 1



async def somefunc():

    while 1:
        if watch_file_update("text.txt"):
            await bot.send_message(config.CHAT_ID, "/question",)



if __name__ == '__main__':
    executor.start(dp, somefunc())