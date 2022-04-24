
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

# @bot.message_handler(content_types=['text'])
# def games(message):
#     if message.text == '🕹️ Game':
#         Game(message)



@bot.message_handler(content_types=['text'])
def base(message):
    if message.text == '🕹️ Game':
        Game(message)

    elif message.text == '📝 Grammar':
        Grammar(message)

    if message.text == '📚 Vocabulary':
        Word(message)
    elif message.text == '📚 Ordinary words':
        ordinary_words(message)

    elif message.text == '📖 Irregular verbs':
        Irregular_verbs(message)

    elif message.text == '📗 Restart':
        Restart_ordinary_words(message)

    elif message.text[0] == '📗':
        number_ordinary_words(message)

    elif message.text == '📕 Restart':
        Restart_Irregular_verbs(message)

    elif message.text[0] == '📕':
        number_Irregular_verbs(message)

    if message.text == 'Полезные ссылки':
        Links(message)

    elif message.text == '🕰️ Time':
        Time(message)

    if message.text == '⬅ Back':
        send_menu(message)

    elif message.text == '⏳Present simple':
        Present_simple(message)


    elif message.text == '⌚Present continuous':
        Present_continuous(message)

    elif message.text == '⏰Present perfect':
        Present_perfect(message)

    elif message.text == '🔞Past simple':
        markup = types.ReplyKeyboardMarkup()
        item1 = types.KeyboardButton('🙈TestFourth')
        item2 = types.KeyboardButton('⬅ Back')
        markup.add(item1, item2)
        bot.send_photo(message.chat.id, "http://grammar-tei.com/wp-content/uploads/2016/10/shema.jpg", reply_markup=markup)

    elif message.text == '🙈TestFourth':
        markup = types.ReplyKeyboardMarkup()
        item1 = types.KeyboardButton('invited')  # Правильный ответ
        item2 = types.KeyboardButton('invite')
        item3 = types.KeyboardButton('inviting')
        item4 = types.KeyboardButton('⬅ Back')
        markup.add(item1, item2, item3, item4)
        bot.send_message(message.chat.id, 'I (to invite) __ your friend to the party.', reply_markup=markup)

        if message.text == 'invited':
            TrueAnswer += 1
            bot.send_message(message.chat.id, 'True answer, my congratulation')

        if message.text == 'invited' or message.text == 'invite' or message.text == 'inviting':
            markup = types.ReplyKeyboardMarkup()
            item1 = types.KeyboardButton('found')  # True answer
            item2 = types.KeyboardButton('finds')
            item3 = types.KeyboardButton('finded')
            item4 = types.KeyboardButton('⬅ Back')
            markup.add(item1, item2, item3, item4)
            bot.send_message(message.chat.id, 'Paul (to find) __ a good and inexpensive hotel.', reply_markup=markup)

        if message.text == 'found':
            TrueAnswer += 1
        bot.send_message(message.chat.id, 'True answer, my congratulation')
    else:
        return


# @bot.message_handler(content_types=['text'])
# def Vocabulary(message):
#     if message.text == '📚 Vocabulary':
#         Word(message)
#     elif message.text == '📚 Ordinary words':
#         ordinary_words(message)
#
#     elif message.text == '📖 Irregular verbs':
#         Irregular_verbs(message)
#
#     elif message.text == '📗 Restart':
#         Restart_ordinary_words(message)
#
#     elif message.text[0] == '📗':
#         number_ordinary_words(message)
#
#     elif message.text == '📕 Restart':
#         Restart_Irregular_verbs(message)
#
#     elif message.text[0] == '📕':
#         number_Irregular_verbs(message)

#
#
# @bot.message_handler(content_types=['text'])
# def useful_links(message):
#     if message.text == 'Полезные ссылки':
#         Links(message)

#
# @bot.message_handler(content_types=['text'])
# def baack(message):
#     if message.text == '⬅ Back':
#         send_menu(message)




bot.polling(none_stop=True)