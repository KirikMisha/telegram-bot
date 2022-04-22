from telebot import TeleBot
from telebot import types
from telebot import re

bot = TeleBot('5317464669:AAG5R6klT_cURjoo0wbbe07mGwtVBu66x6Y')
with open('./Wordss/words.txt', encoding='utf-8') as inp:
    words = inp.readlines()

with open('./Wordss/IrregularVerbs.txt', encoding='utf-8') as inp:
    Iwords = inp.readlines()



@bot.message_handler(commands=['menu'])
def menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('🕹️ Game')
    item2 = types.KeyboardButton('📝 Grammar')
    item3 = types.KeyboardButton('📚 Vocabulary')
    item4 = types.KeyboardButton('Полезные ссылки')
    markup.add(item1, item2, item3, item4)
    bot.send_message(message.chat.id, '🗂️ Menu', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def menu(message):
    if message.text == '🕹️ Game':
        markup = types.ReplyKeyboardMarkup()
        item1 = types.KeyboardButton('🐊 Crocodile')
        item2 = types.KeyboardButton('Word Game')
        item3 = types.KeyboardButton('⬅ Back')
        markup.add(item1, item2, item3)
        bot.send_message(message.chat.id, 'описание раздела игр', reply_markup=markup)
    elif message.text == '📝 Grammar':
        markup = types.ReplyKeyboardMarkup()
        item1 = types.KeyboardButton('🕰️ Time')
        item2 = types.KeyboardButton('👮‍♂ Rules')
        item3 = types.KeyboardButton('⬅ Back')
        markup.add(item1, item2, item3)
        bot.send_message(message.chat.id, 'описание граматики', reply_markup=markup)
    elif message.text == '📚 Vocabulary':
        markup = types.ReplyKeyboardMarkup()
        item1 = types.KeyboardButton('📚 Words')
        item2 = types.KeyboardButton('📖 Irregular verbs')
        item3 = types.KeyboardButton('💁‍♂ Basic stable expressions')
        item4 = types.KeyboardButton('⬅ Back')
        markup.add(item1, item2, item3,item4)
        bot.send_message(message.chat.id, 'описание слов', reply_markup=markup)
    elif message.text == 'Полезные ссылки':
        bot.send_message(message.chat.id, 'Ссылки')
    elif message.text == '📚 Words':
        markup = types.ReplyKeyboardMarkup()
        item1 = types.KeyboardButton('📗 1')
        item2 = types.KeyboardButton('📗 5')
        item3 = types.KeyboardButton('📗 10')
        item4 = types.KeyboardButton('⬅ Back')
        markup.add(item1, item2, item3, item4)
        bot.send_message(message.chat.id, 'В этом разделе ты выберешь сколько слов я тебе выдам на заучивание сегодня.'
                                          'Оптимальным вариантом будет учить по 5-10 слов в день,'
                                          ' однако главным в этом деле, учить хотя бы одно слово-это уже прогресс.\n'
                                          'p.s. ( при выборе желаемого количества слов напиши в чат 📗 *пробел* цифра)'
                                          '', reply_markup=markup)
    elif message.text == '📖 Irregular verbs':
        markup = types.ReplyKeyboardMarkup()
        item1 = types.KeyboardButton('📕 1')
        item2 = types.KeyboardButton('📕 2')
        item3 = types.KeyboardButton('📕 3')
        item4 = types.KeyboardButton('⬅ Back')
        markup.add(item1, item2, item3, item4)
        bot.send_message(message.chat.id, 'В этом разделе ты выберешь сколько неправильных глаголов я тебе выдам на '
                                          'заучивание сегодня.'
                                          'Оптимальным вариантом будет учить по 5-10 слов в день,'
                                          ' однако главным в этом деле, учить хотя бы одно слово-это уже прогресс.\n'
                                          'p.s. ( при выборе желаемого количества слов напиши в чат 📕 *пробел* цифра)'
                                          '', reply_markup=markup)
    elif message.text == '⬅ Back':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('🕹️ Game')
        item2 = types.KeyboardButton('📝 Grammar')
        item3 = types.KeyboardButton('📚 Vocabulary')
        item4 = types.KeyboardButton('Полезные ссылки')
        markup.add(item1, item2, item3, item4)
        bot.send_message(message.chat.id, '🗂️ Menu', reply_markup=markup)
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





# @bot.message_handler()
# def Wordsss(message):
#     if message.text[0] == '📗':
#         if message.text.replace('📗 ', '').isdigit():
#             number = int(message.text.replace('📗 ', ''))
#             for i in range(number):
#                 bot.send_message(message.chat.id, words[i])
#         else:
#             bot.send_message(message.chat.id, 'Enter a number')
#     elif message.text[0] == '📕':
#         if message.text.replace('📕 ', '').isdigit():
#             number = int(message.text.replace('📕 ', ''))
#             for i in range(number):
#                 bot.send_message(message.chat.id, Iwords[i])
#         else:
#             bot.send_message(message.chat.id, 'Enter a number')


bot.polling(none_stop=True)
