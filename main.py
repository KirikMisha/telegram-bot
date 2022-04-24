from telebot import *
from config import BOT_TOKEN
import sqlite3
from Game.Game import *
from Grammar.Grammar import *
from Vocabulary.Words import *
from Links.Links import *
from db import Base

bot = TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_start(message):
    Base(message)


@bot.message_handler(commands=['menu'])
def send_menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('🕹️ Game')
    item2 = types.KeyboardButton('📝 Grammar')
    item3 = types.KeyboardButton('📚 Vocabulary')
    item4 = types.KeyboardButton('Полезные ссылки')
    markup.add(item1, item2, item3, item4)
    bot.send_message(message.chat.id, '🗂️ Menu', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def base(message):
    if message.text == '🕹️ Game':
        Game(message)

    elif message.text == '📝 Grammar':
        Grammar(message)

    elif message.text == '📚 Vocabulary':
        Word(message)

    elif message.text == 'Полезные ссылки':
        Links(message)

    elif message.text == '📚 Words':
        Words(message)

    elif message.text == '📖 Irregular verbs':
        Irregular_verbs(message)

    elif message.text == '⬅ Back':
        send_menu(message)

    elif message.text[0] == '📗':
        if message.text.replace('📗 ', '').isdigit():
            number = int(message.text.replace('📗 ', ''))
            for i in range(number):
                bot.send_message(message.chat.id, words[i])
        else:
            bot.send_message(message.chat.id, 'Enter a number')
    elif message.text[0] == '📕':
        if message.text.replace('📕 ', '').isdigit():
            number = int(message.text.replace('📕 ', ''))
            for i in range(number):
                bot.send_message(message.chat.id, Iwords[i])
        else:
            bot.send_message(message.chat.id, 'Enter a number')
    elif message.text == '🕰️ Time':
        Time(message)

    elif message.text == '⏳Present simple':
        markup = types.ReplyKeyboardMarkup()
        item1 = types.KeyboardButton('🙈TestFirst')
        item2 = types.KeyboardButton('⬅ Back')
        markup.add(item1, item2)
        bot.send_photo(message.chat.id, "http://lingvana.ru/wp-content/uploads/2014/03/Tablitsa-past-simpl-skan.png", reply_markup=markup)
    elif message.text == '⌚Present continuous':
        markup = types.ReplyKeyboardMarkup()
        item1 = types.KeyboardButton('🙈TestSecond')
        item2 = types.KeyboardButton('⬅ Back')
        markup.add(item1, item2)
        bot.send_photo(message.chat.id, "https://preply.com/wp-content/uploads/2018/04/Tablitsa-prezent-kontinius-2.jpg", reply_markup=markup)
    elif message.text == '⏰Present perfect':
        markup = types.ReplyKeyboardMarkup()
        item1 = types.KeyboardButton('🙈TestTheThird')
        item2 = types.KeyboardButton('⬅ Back')
        markup.add(item1, item2)
        bot.send_photo(message.chat.id, "https://www.englishdom.com/dynamicus/blog-post/000/001/329/1526281369.556_700x445_content.jpg", reply_markup=markup)
    elif message.text == '🔞Past simple':
        markup = types.ReplyKeyboardMarkup()
        item1 = types.KeyboardButton('🙈TestFourth')
        item2 = types.KeyboardButton('⬅ Back')
        markup.add(item1, item2)
        bot.send_photo(message.chat.id, "http://grammar-tei.com/wp-content/uploads/2016/10/shema.jpg", reply_markup=markup)
    elif message.text == '🙈TestFourth':
        markup = types.ReplyKeyboardMarkup()
        item1 = types.KeyboardButton('invited')
        item2 = types.KeyboardButton('invite')
        item3 = types.KeyboardButton('inviting')
        item4 = types.KeyboardButton('⬅ Back')
        markup.add(item1, item2, item3, item4)
        bot.send_message(message.chat.id, 'I (to invite) __ your friend to the party.', reply_markup=markup)


bot.polling(none_stop=True)