import os
from dotenv import load_dotenv
import telebot

# load envinroment variables from the .env file
load_dotenv()

# set up the environment
BOT_TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)

# init bot
@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "How are you doing?")

# loop bot
@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, message.text)

# launch bot
bot.infinity_polling()
