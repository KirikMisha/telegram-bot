from aiogram.dispatcher import FSMContext
from config import bot, Dispatcher, dp
from aiogram import types
from db import Plass, Restart_ordinary_words
from aiogram.dispatcher.filters.state import State, StatesGroup


class how_many_words(StatesGroup):
    test1 = State()
    test2 = State()
    test3 = State()


with open('./Vocabulary/Ordinary_words.txt', encoding='utf-8') as inp:
    Owords = inp.readlines()


# Развертка меню строк---------------------------------------------------------------------------------------------------
async def vocabulary(message: types.Message):
    item1 = types.KeyboardButton('📚 Ordinary words')
    item2 = types.KeyboardButton('📖 Irregular verbs')
    item3 = types.KeyboardButton('💁‍♂ Basic stable expressions')
    item4 = types.KeyboardButton('⬅ Back to menu')
    markup = types.ReplyKeyboardMarkup()
    markup.add(item1, item2, item3, item4)
    await bot.send_message(message.chat.id, 'описание слов', reply_markup=markup)


#-----------------------------------------------------------------------------------------------------------------------


#Вывод обычных слов-----------------------------------------------------------------------------------------------------
async def ordinary_words(message: types.Message):
    item1 = types.KeyboardButton('📗 1')
    item2 = types.KeyboardButton('📗 5')
    item3 = types.KeyboardButton('📗 10')
    item4 = types.KeyboardButton('⬅ Back to menu')
    markup = types.ReplyKeyboardMarkup()
    markup.add(item1, item2, item3, item4)
    await bot.send_message(message.chat.id, 'В этом разделе ты выберешь сколько слов я тебе выдам на заучивание '
                                            'сегодня.Оптимальным вариантом будет учить по 5-10 слов в день, однако '
                                            'главным в этом деле, учить хотя бы одно слово-это уже прогресс.\n'
                                            'p.s. ( при выборе желаемого количества слов напиши в чат 📗 *пробел* '
                                            'цифра)\np.p.s. (если хочешь начать с самого начала вбей команду: 📗 '
                                            'Restart)'
                                            '', reply_markup=markup)
    await how_many_words.test1.set()


@dp.message_handler(state=how_many_words.test1)
async def ordinary(message: types.Message):
    if message.text[0] == '📙':
        if message.text.replace('📗 ', '').isdigit():
            number = int(message.text.replace('📗 ', ''))
            i = Plass(message, number)
            number = i + number
            while i < number:
                i = i + 1
                bot.send_message(message.chat.id, Owords[i])
                if i == 1415:
                    await bot.send_message(message.chat.id, 'Молодец, ты выучил весь Английский )')
                    await bot.send_photo(message.chat.id,
                                         'http://risovach.ru/upload/2014/03/mem/forever-alone_46449071_orig_.jpg')
                    await Restart_ordinary_words(message)
                    break
        else:
            await bot.send_message(message.chat.id, 'Enter a number\n'
                                                    'Example:📗 [number]')


#-----------------------------------------------------------------------------------------------------------------------


#Вывод неправильных глаголов--------------------------------------------------------------------------------------------
async def irregular_verbs(message: types.Message):
    item1 = types.KeyboardButton('📕 1')
    item2 = types.KeyboardButton('📕 3')
    item3 = types.KeyboardButton('📕 5')
    item4 = types.KeyboardButton('⬅ Back to menu')
    markup = types.ReplyKeyboardMarkup()
    markup.add(item1, item2, item3, item4)
    await bot.send_message(message.chat.id, 'В этом разделе ты выберешь сколько неправильных глаголов я тебе '
                                            'выдам на заучивание сегодня.Оптимальным вариантом будет учить по 5-10 '
                                            'слов в день, однако главным в этом деле, учить хотя бы одно слово-это '
                                            'уже прогресс.\np.s. ( при выборе желаемого количества слов напиши в '
                                            'чат 📕 *пробел* цифра)p.p.s. (если хочешь начать с самого начала вбей '
                                            'команду: 📕 Restart)'
                                            '', reply_markup=markup)


# ----------------------------------------------------------------------------------------------------------------------


# Вывод базовых устойчивых выражений------------------------------------------------------------------------------------
async def basic_stable_expressions(message: types.Message):
    item1 = types.KeyboardButton('📙 1')
    item2 = types.KeyboardButton('📙 3')
    item3 = types.KeyboardButton('📙 5')
    item4 = types.KeyboardButton('⬅ Back to menu')
    markup = types.ReplyKeyboardMarkup()
    markup.add(item1, item2, item3, item4)
    await bot.send_message(message.chat.id, 'В этом разделе ты выберешь сколько базовых устойчивых выражений '
                                            'английского языка я тебе выдам на заучивание сегодня.Оптимальным '
                                            'вариантом будет учить по 5-10 слов в день, однако главным в этом '
                                            'деле, учить хотя бы одно слово-это уже прогресс.\np.s. ( при выборе '
                                            'желаемого количества слов напиши в чат 📙 *пробел* цифра)p.p.s. (если '
                                            'хочешь начать с самого начала вбей команду: 📙 Restart)'
                                            '', reply_markup=markup)


#-----------------------------------------------------------------------------------------------------------------------


def expanded_vocabulary_f(dp: Dispatcher):
    dp.register_callback_query_handler(vocabulary, text='📚 Vocabulary')
    dp.register_callback_query_handler(ordinary_words, text='📚 Ordinary words')
    dp.register_callback_query_handler(irregular_verbs, text='📖 Irregular verbs')
    dp.register_callback_query_handler(basic_stable_expressions, text='💁‍♂ Basic stable expressions')
