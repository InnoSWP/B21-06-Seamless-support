import logging
from random import randint
from datetime import datetime, timedelta

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

import config

bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

# дописать получение данных с web страницы, по дефолту стоят эти
USER_NAME = "Иван"
USER_QUESTION = "Как оплатить заказ?"

# по команде /example запускатеся работа бота с дефолтными данными

def forward_to_user(update, context):
    user_id = None
    if update.message.reply_to_message.forward_from:
        user_id = update.message.reply_to_message.forward_from.id
    # elif REPLY_TO_THIS_MESSAGE in update.message.reply_to_message.text:
    #     try:
    #         user_id = int(update.message.reply_to_message.text.split('\n')[0])
    #     except ValueError:
    #         user_id = None
    if user_id:
        context.bot.copy_message(
            message_id=update.message.message_id,
            chat_id=user_id,
            from_chat_id=update.message.chat_id
        )
    else:
        context.bot.send_message(
            chat_id=-799113402,
            text="WRONG_REPLY"
        )

@dp.message_handler(commands="example")
async def cmd_random(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Принять ✅", callback_data="accept"))
    keyboard.add(types.InlineKeyboardButton(text="Отклонить ❌", callback_data="decline"))
    await message.answer("Новый вопрос\nИмя: " + USER_NAME + "\nВопрос: " + USER_QUESTION, reply_markup=keyboard)


@dp.callback_query_handler(text="accept")
async def send_random_value(call: types.CallbackQuery):
    volounteer_id = call.from_user.id
    volounteer_name = call.from_user.first_name

    await call.message.answer("Вопрос был принят " + volounteer_name)
    await bot.send_message(volounteer_id, "Вопрос от " + USER_NAME + "\n" + USER_QUESTION)

    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Начать помогать", callback_data="start"))
    keyboard.add(types.InlineKeyboardButton(text="Закончить помогать", callback_data="finish"))
    await bot.send_message(volounteer_id, "Выберите действие", reply_markup=keyboard)

    @dp.callback_query_handler(text="start")
    async def start_help(call: types.CallbackQuery):
        await bot.send_message(volounteer_id, "Напишите решение проблемы")

    @dp.callback_query_handler(text="finish")
    async def finish_help(call: types.CallbackQuery):
        await bot.send_message(volounteer_id, "Ваш ответ отправлен\nСпасибо!")
        await call.message.delete()

        # TODO: тут нужно прописать как происходит отправка ответа пользователю/в бд

        forward_to_user()

    await call.message.delete()


@dp.callback_query_handler(text="decline")
async def send_random_value(call: types.CallbackQuery):
    volounteer_name = call.from_user.first_name
    await call.message.answer("Вопрос был отклонен " + volounteer_name)


executor.start_polling(dp, skip_updates=True)
