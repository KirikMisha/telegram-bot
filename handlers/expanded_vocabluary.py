from config import bot, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, Message, ReplyKeyboardMarkup, \
    KeyboardButton
from aiogram.dispatcher import filters
from db import plass, restart_words

# Заполняем списки строками из файлов-----------------------------------------------------------------------------------
with open('./Vocabulary/Ordinary_words.txt', encoding='utf-8') as inp:
    o_words = inp.readlines()

with open('./Vocabulary/IrregularVerbs.txt', encoding='utf-8') as inp:
    i_words = inp.readlines()

with open('./Vocabulary/Stable_expressions.txt', encoding='utf-8') as inp:
    b_words = inp.readlines()


# ----------------------------------------------------------------------------------------------------------------------
41

# Развёртка меню строк--------------------------------------------------------------------------------------------------
async def vocabulary_menu(callback: CallbackQuery):
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    item1 = InlineKeyboardButton('📚 Ordinary words', callback_data='ordinary_words')
    item2 = InlineKeyboardButton('📖 Irregular verbs', callback_data='irregular_verbs')
    item3 = InlineKeyboardButton('💁‍ Basic stable expressions', callback_data='basic_stable_expressions')
    item4 = InlineKeyboardButton('⬅ Back to menu', callback_data='back_menu')
    markup = InlineKeyboardMarkup(row_width=2)
    markup.add(item1, item2, item3, item4)
    await callback.message.answer('В этом разделе ты сможешь изучать неправильне глаголы, более 1000 слов английского '
                                  'языка которые 100% понядобятся тебе на практике и базовые устойчивые выражения '
                                  'которые чаще всего используют носители языка ', reply_markup=markup)


# ----------------------------------------------------------------------------------------------------------------------


# Развёртка меню обычных слов-------------------------------------------------------------------------------------------
async def ordinary_words(callback: CallbackQuery):
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    item1 = KeyboardButton('📗 1')
    item2 = KeyboardButton('📗 5')
    item3 = KeyboardButton('📗 10')
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    markup.add(item1, item2, item3)
    await callback.message.answer('В этом разделе ты выберешь сколько слов я тебе выдам на заучивание сегодня.'
                                  'Оптимальным вариантом будет учить по 5-10 слов в день, однако главным в этом деле, '
                                  'учить хотя бы одно слово-это уже прогресс.\np.s. ( при выборе желаемого количества '
                                  'слов напиши в чат 📗 *пробел* цифра)\np.p.s. (если хочешь начать с самого начала '
                                  'вбей команду: 📗 Restart)', reply_markup=markup)


# ----------------------------------------------------------------------------------------------------------------------


# Развёртка меню неправильных глаголов----------------------------------------------------------------------------------
async def irregular_verbs(callback: CallbackQuery):
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    item1 = KeyboardButton('📕 1')
    item2 = KeyboardButton('📕 3')
    item3 = KeyboardButton('📕 5')
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    markup.add(item1, item2, item3)
    await callback.message.answer('В этом разделе ты выберешь сколько неправильных глаголов я тебе выдам на заучивание '
                                  'сегодня.Оптимальным вариантом будет учить по 5-10 слов в день, однако главным в этом'
                                  ' деле, учить хотя бы одно слово-это уже прогресс.\np.s. ( при выборе желаемого '
                                  'количества слов напиши в чат 📕 *пробел* цифра)\np.p.s. (если хочешь начать с самого '
                                  'начала вбей команду: 📕 Restart)', reply_markup=markup)


# ----------------------------------------------------------------------------------------------------------------------


# Развёртка меню базовых устойчивых выражений---------------------------------------------------------------------------
async def basic_stable_expressions(callback: CallbackQuery):
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    item1 = KeyboardButton('📙 1')
    item2 = KeyboardButton('📙 3')
    item3 = KeyboardButton('📙 5')
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    markup.add(item1, item2, item3)
    await callback.message.answer('В этом разделе ты выберешь сколько базовых устойчивых выражений английского языка я '
                                  'тебе выдам на заучивание сегодня.Оптимальным вариантом будет учить по 5-10 слов в '
                                  'день, однако главным в этом деле, учить хотя бы одно слово-это уже прогресс.\np.s. '
                                  '( при выборе желаемого количества слов напиши в чат 📙 *пробел* цифра)\np.p.s. (если '
                                  'хочешь начать с самого начала вбей команду: 📙 Restart)', reply_markup=markup)


# ----------------------------------------------------------------------------------------------------------------------


# Вывод слов------------------------------------------------------------------------------------------------------------
async def word_output(message: Message):
    global column, number_of_words, words
    if message.text[0] == '📗':
        if message.text.replace('📗 ', '').isdigit():
            number_of_words = int(message.text.replace('📗 ', ''))
            column = 'number_ordinary_words'
            words = o_words
    elif message.text[0] == '📕':
        if message.text.replace('📕 ', '').isdigit():
            number_of_words = int(message.text.replace('📕 ', ''))
            column = 'number_Irregular_verbs'
            words = i_words
    elif message.text[0] == '📙':
        if message.text.replace('📙 ', '').isdigit():
            number_of_words = int(message.text.replace('📙 ', ''))
            column = 'number_Basic_stable_expressions'
            words = b_words
    else:
        bot.send_message(message.chat.id, 'Enter a number\n'
                                          'Example:(📗 or 📕 or 📙) [number]')
    i = plass(message, column, number_of_words)
    number_of_words += i
    while i < number_of_words:
        await bot.send_message(message.chat.id, words[i])
        i = i + 1
        if i == len(words):
            await bot.send_message(message.chat.id, 'Молодец, ты выучил весь Английский )')
            await bot.send_photo(message.chat.id,
                                 'http://risovach.ru/upload/2014/03/mem/forever-alone_46449071_orig_.jpg')
            await restart_words(message, column)
            break
    item = KeyboardButton('⬅ Back', callback_data='vocabulary_menu')
    markup = InlineKeyboardMarkup()
    markup.add(item)
    await message.answer(f'Вот тебе подборка слов на сегодня, удачного изучения\np.s (ты уже дошёл до {number_of_words}'
                         f' слова)', reply_markup=markup)


# ----------------------------------------------------------------------------------------------------------------------


# Register hendlers-----------------------------------------------------------------------------------------------------
def expanded_vocabulary_f(dp: Dispatcher):
    dp.register_callback_query_handler(vocabulary_menu, text='vocabulary_menu')
    dp.register_callback_query_handler(ordinary_words, text='ordinary_words')
    dp.register_callback_query_handler(irregular_verbs, text='irregular_verbs')
    dp.register_callback_query_handler(basic_stable_expressions, text='basic_stable_expressions')
    dp.register_message_handler(word_output, filters.Text(startswith='📗') |
                                filters.Text(startswith='📕') |
                                filters.Text(startswith='📙'))
# -----------------------------------------------------------------------------------------------------------------------
