from telebot import types
from telebot import TeleBot
from config import BOT_TOKEN
from db import *


bot = TeleBot(BOT_TOKEN)

with open('./Vocabulary/words.txt', encoding='utf-8') as inp:
    words = inp.readlines()

with open('./Vocabulary/IrregularVerbs.txt', encoding='utf-8') as inp:
    Iwords = inp.readlines()

def Word(message):
    markup = types.ReplyKeyboardMarkup()
    item1 = types.KeyboardButton('📚 Ordinary words')
    item2 = types.KeyboardButton('📖 Irregular verbs')
    item3 = types.KeyboardButton('💁‍♂ Basic stable expressions')
    item4 = types.KeyboardButton('⬅ Back')
    markup.add(item1, item2, item3, item4)
    bot.send_message(message.chat.id, 'описание слов', reply_markup=markup)

def ordinary_words(message):
    markup = types.ReplyKeyboardMarkup()
    item1 = types.KeyboardButton('📗 1')
    item2 = types.KeyboardButton('📗 5')
    item3 = types.KeyboardButton('📗 10')
    item4 = types.KeyboardButton('⬅ Back')
    markup.add(item1, item2, item3, item4)
    bot.send_message(message.chat.id, 'В этом разделе ты выберешь сколько слов я тебе выдам на заучивание сегодня.'
                                      'Оптимальным вариантом будет учить по 5-10 слов в день,'
                                      ' однако главным в этом деле, учить хотя бы одно слово-это уже прогресс.\n'
                                      'p.s. ( при выборе желаемого количества слов напиши в чат 📗 *пробел* цифра)\n'
                                      'p.p.s. (если хочешь начать с самого начала вбей команду: 📗 *пробел* Restart)'
                                      '', reply_markup=markup)
def Irregular_verbs(message):
    markup = types.ReplyKeyboardMarkup()
    item1 = types.KeyboardButton('📕 1')
    item2 = types.KeyboardButton('📕 3')
    item3 = types.KeyboardButton('📕 5')
    item4 = types.KeyboardButton('⬅ Back')
    markup.add(item1, item2, item3, item4)
    bot.send_message(message.chat.id, 'В этом разделе ты выберешь сколько неправильных глаголов я тебе выдам на '
                                      'заучивание сегодня.'
                                      'Оптимальным вариантом будет учить по 5-10 слов в день,'
                                      ' однако главным в этом деле, учить хотя бы одно слово-это уже прогресс.\n'
                                      'p.s. ( при выборе желаемого количества слов напиши в чат 📕 *пробел* цифра)'
                                      '', reply_markup=markup)
def number_ordinary_words(message):
    if message.text.replace('📗 ', '').isdigit():
        number = int(message.text.replace('📗 ', ''))
        i = Plass(message,number)
        number = i + number
        while i < number:
            i = i + 1
            bot.send_message(message.chat.id, words[i])
    else:
        bot.send_message(message.chat.id, 'Enter a number\n'
                                          'Example:📗 [number]')

def number_Irregular_verbs(message):
    if message.text.replace('📕 ', '').isdigit():
        number = int(message.text.replace('📕 ', ''))
        i = PlassI(message, number)
        number = i + number
        while i < number:
            i = i + 1
            bot.send_message(message.chat.id, Iwords[i])
    else:
        bot.send_message(message.chat.id, 'Enter a number\n'
                                          'Example:📗 [number]')