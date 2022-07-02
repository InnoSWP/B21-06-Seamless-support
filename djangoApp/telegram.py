import logging
import os
import config
import django
from aiogram import Bot, Dispatcher, executor, filters, types
from core.Database.database import GoogleSheets as Database

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangoApp.settings")

django.setup()


bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)
gs = Database()


@dp.message_handler(filters.Text(contains="Получить вопрос", ignore_case=True))
async def cmd_random(message: types.Message):
    mess = gs.peek_message_from_queue()
    USER_NAME = mess[0]
    USER_QUESTION = mess[1]

    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Принять ✅", callback_data="accept"))
    keyboard.add(
        types.InlineKeyboardButton(text="Отклонить ❌", callback_data="decline")
    )
    await message.answer(
        "Имя: " + USER_NAME + "\nВопрос: " + USER_QUESTION, reply_markup=keyboard
    )


@dp.callback_query_handler(filters.Text(contains="accept", ignore_case=True))
async def send_random_value(call: types.CallbackQuery):
    mess = gs.pop_message_from_queue()
    USER_NAME = mess[0]
    USER_QUESTION = mess[1]

    volounteer_id = call.from_user.id
    volounteer_name = call.from_user.first_name

    await call.message.answer("Вопрос был принят " + volounteer_name)
    await bot.send_message(
        volounteer_id, "Вопрос от " + USER_NAME + "\n" + USER_QUESTION
    )

    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(
        types.InlineKeyboardButton(text="Начать помогать", callback_data="start")
    )
    keyboard.add(
        types.InlineKeyboardButton(text="Закончить помогать", callback_data="finish")
    )
    await bot.send_message(volounteer_id, "Выберите действие", reply_markup=keyboard)

    @dp.callback_query_handler(text="start")
    async def start_help(call: types.CallbackQuery):
        await bot.send_message(volounteer_id, "Напишите решение проблемы")

    @dp.callback_query_handler(filters.Text(contains="finish", ignore_case=True))
    async def finish_help(call: types.CallbackQuery):
        await bot.send_message(volounteer_id, "Ваш ответ отправлен\nСпасибо!")

        await call.message.delete()

        # TODO: тут нужно прописать как происходит отправка ответа пользователю/в бд

    await call.message.delete()

    @dp.message_handler()
    async def get_answer(message: types.Message):
        file_answer = open("answer.txt", "w")
        file_answer.write(message.text)
        file_answer.close()
        # add_answers(message=message.text, vol_id=str(message.from_user.id))


@dp.callback_query_handler(text="decline")
async def send_random_value_dec(call: types.CallbackQuery):
    volounteer_name = call.from_user.first_name
    await call.message.answer("Вопрос был отклонен " + volounteer_name)


executor.start_polling(dp, skip_updates=True)
