from telebot import types
from telebot import TeleBot
from config import BOT_TOKEN
bot = TeleBot(BOT_TOKEN)

def Game(message):
    markup = types.ReplyKeyboardMarkup()
    item1 = types.KeyboardButton('🐊 Crocodile')
    item2 = types.KeyboardButton('Word Game')
    item3 = types.KeyboardButton('⬅ Back')
    markup.add(item1, item2, item3)
    bot.send_message(message.chat.id, 'описание раздела игр', reply_markup=markup)
