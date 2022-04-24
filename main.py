from telebot import *
from config import BOT_TOKEN
import sqlite3
from Game.Game import *
from Grammar.Grammar import *
from db import Base

bot = TeleBot(BOT_TOKEN)

with open('./Vocabulary/words.txt', encoding='utf-8') as inp:
    words = inp.readlines()

with open('./Vocabulary/IrregularVerbs.txt', encoding='utf-8') as inp:
    Iwords = inp.readlines()


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
        markup = types.ReplyKeyboardMarkup()
        item1 = types.KeyboardButton('⏳Present simple',)
        item2 = types.KeyboardButton('⌚Present continuous')
        item3 = types.KeyboardButton('⏰Present perfect')
        item4 = types.KeyboardButton('🔞Past simple')
        item5 = types.KeyboardButton('⬅ Back')
        markup.add(item1, item2, item3, item4, item5)
        bot.send_message(message.chat.id, 'описание граматики', reply_markup=markup)
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