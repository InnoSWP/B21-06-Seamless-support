import logging
import os

from telebot.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, KeyboardButton, \
    ReplyKeyboardMarkup

import config
import django
import telebot
from core.Database.database import gs

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangoApp.settings")


bot = telebot.TeleBot(token=config.TOKEN)
# dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)


def send_question_available():
    button_hi = KeyboardButton('Get question')

    greet_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    greet_kb.add(button_hi)

    bot.send_message(chat_id=config.CHAT_ID, text="NEW QUESTION AVAILABLE\n", reply_markup=greet_kb)


@bot.message_handler(func=lambda m: m.text == "Get question")
def cmd_random(message: Message):
    mess = gs.peek_message_from_queue()
    USER_NAME = mess[0]
    USER_QUESTION = mess[1]

    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton(text="Accept ✅", callback_data="accept"))
    keyboard.add(
        InlineKeyboardButton(text="Decline ❌", callback_data="decline")
    )
    bot.send_message(
        config.CHAT_ID,
        "Name: " + USER_NAME + "\nQuestion: " + USER_QUESTION, reply_markup=keyboard
    )


@bot.callback_query_handler(func=lambda q: q.data == 'accept')
def send_random_value(call: CallbackQuery):
    mess = gs.pop_message_from_queue()
    USER_NAME = mess[0]
    USER_QUESTION = mess[1]

    volunteer_id = call.from_user.id
    volunteer_name = call.from_user.first_name

    bot.delete_message(chat_id=config.CHAT_ID, message_id=call.message.message_id)
    bot.send_message(chat_id=config.CHAT_ID, text="The question was picked by " + volunteer_name)
    bot.send_message(
        volunteer_id, "Question from " + USER_NAME + "\n" + USER_QUESTION
    )

    keyboard = InlineKeyboardMarkup()
    keyboard.add(
        InlineKeyboardButton(text="Start help", callback_data="start")
    )
    keyboard.add(
        InlineKeyboardButton(text="Finish help", callback_data="finish")
    )
    bot.send_message(volunteer_id, "Choose the option", reply_markup=keyboard)

    @bot.callback_query_handler(func=lambda q: q.data == 'start')
    def start_help(call: CallbackQuery):
        bot.send_message(volunteer_id, "Write your solution")

    @bot.callback_query_handler(func=lambda q: q.data == 'finish')
    def finish_help(call: CallbackQuery):
        bot.send_message(volunteer_id, "Your answer was sent\nThank you!")

    @bot.message_handler()
    def get_answer(message: Message):
        file_answer = open("answer.txt", "w")
        file_answer.write(message.text)
        file_answer.close()
        # add_answers(message=message.text, vol_id=str(message.from_user.id))


@bot.callback_query_handler(func=lambda q: q.data == 'decline')
async def send_random_value_dec(call: CallbackQuery):
    volunteer_name = call.from_user.first_name
    bot.delete_message(chat_id=config.CHAT_ID, message_id=call.message.message_id)
    bot.send_message(chat_id=config.CHAT_ID, text="Вопрос был отклонен " + volunteer_name)


if __name__ == "__main__":
    bot.infinity_polling()
