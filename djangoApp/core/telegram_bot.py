import telebot
import asyncio


TOKEN = '5530222336:AAFwwgeougdlbekmH83_epwYlU-fmUGxoL4'
bot = telebot.TeleBot(TOKEN)
chats = ['-799113402']


@bot.message_handler(commands=['start'])
def start(message):
    if message.chat.id not in chats:
        chats.append(message.chat.id)
        print(f'Activated in {message.chat.id}')
    bot.send_message(message.chat.id, "Activated")


async def bot_message(content):
    for chat_id in chats:
        bot.send_message(chat_id, content)


def run_bot():
    print('Bot started')
    bot.infinity_polling()




