from config import bot, Dispatcher, words_game, crocodile_game
from aiogram.dispatcher import FSMContext
from aiogram import types
import random
import enchant


# Развертка меню игр----------------------------------------------------------------------------------------------------
async def game_menu(callback: types.CallbackQuery):
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    item1 = types.InlineKeyboardButton('🐊 Crocodile', callback_data='crocodile')
    item2 = types.InlineKeyboardButton('Word Game', callback_data='word_game')
    item3 = types.InlineKeyboardButton('⬅ Back to menu', callback_data='back_menu')
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(item1, item2, item3)
    await callback.message.answer('описание раздела игр', reply_markup=markup)


# ----------------------------------------------------------------------------------------------------------------------


# Игра в слова----------------------------------------------------------------------------------------------------------
dictionary = enchant.Dict("en")
words_used = []


async def word_game(callback: types.CallbackQuery):
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    item1 = types.InlineKeyboardButton('Let\'s go', callback_data='first_word_user_words_game')
    item2 = types.InlineKeyboardButton('⬅ Back to menu', callback_data='back_menu')
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(item1, item2)
    await callback.message.answer('Привет, это меню игры в слова, по очереди ты с ботом соревнуешься в знании '
                                  'английских слов, вы по очереди должны писать по одному слову, начинающигося '
                                  'на букву, которой заканчивается предыдущее слово \n'
                                  'Ты согласен продолжить, или вернешься назад?', reply_markup=markup)


async def first_word_user_words_game(callback: types.CallbackQuery):
    await bot.send_message(callback.message.chat.id, 'Well, if you agree, let\'s start. \n'
                                                     'p.s(just write any word from English)')
    await words_game.first_word_user.set()


async def first_word_bot_words_game(message: types.Message, state: FSMContext):
    if dictionary.check(message.text):

        words_bot = random_word_words_game(message.text)

        words_used.append(message.text)
        words_used.append(words_bot)

        last_letter = words_bot[0][-1]

        await bot.send_message(message.chat.id, words_bot[0])
        await bot.send_message(message.chat.id,
                               f'It\'s your turn, the word should start with <b><u>{last_letter}</u></b>'
                               f'', parse_mode='html')
        await state.update_data(first_word_user=last_letter[0])
        await words_game.first_word_bot.set()
    else:
        await bot.send_message(message.chat.id, f'This won\'t do, there is no such word in the English language.\n'
                                                f'Try again', parse_mode='html')
        await words_game.first_word_user.set()


async def main_words_game(message: types.Message, state: FSMContext):
    data = await state.get_data()
    last_letter_first = data.get('first_word_user')

    if dictionary.check(message.text):

        if message.text[0].upper() != last_letter_first.upper():
            await bot.send_message(message.chat.id, f'That won\'t do, your word should start with: '
                                                    f'<b><u>{last_letter_first}</u></b>', parse_mode='html')
            await words_game.first_word_bot.set()
            return

        if message.text in words_used:
            await bot.send_message(message.chat.id, f'There has already been such a word, try another one'
                                                    f'', parse_mode='html')
            await words_game.first_word_bot.set()
            return

        words_bot = random_word_words_game(message.text)

        words_used.append(message.text)
        words_used.append(words_bot)

        last_letter = words_bot[0][-1]

        if words_bot == 'Поздравляю, тебе удалось победить':
            await bot.send_message(message.chat.id, words_bot)
            await state.finish()

        else:
            await bot.send_message(message.chat.id, words_bot[0])
            await bot.send_message(message.chat.id,
                               f'It\'s your turn, the word should start with <b><u>{last_letter}</u></b>'
                               f'', parse_mode='html')
        await state.update_data(first_word_user=last_letter)
        await words_game.first_word_bot.set()

    else:
        await bot.send_message(message.chat.id, f'This won\'t do, there is no such word in the English language.\n'
                                                f'Try again', parse_mode='html')
        await words_game.first_word_bot.set()


def random_word_words_game(word):
    with open(f'./Game/Words_to_words_game/{word[-1].upper()}.txt', encoding='utf-8') as inp:
        letter = inp.readlines()

    try:
        last_letter = letter[random.randint(0, len(letter))].split('\t')
    except Exception:
        last_letter = 'Поздравляю, тебе удалось победить'

    if last_letter in words_used:
        words_bot = random_word_words_game(word)
        word = words_bot
    else: word = last_letter

    return word


# ----------------------------------------------------------------------------------------------------------------------


# Развертка игры крокодила----------------------------------------------------------------------------------------------
async def crocodile_gamee(callback: types.CallbackQuery):
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    item1 = types.InlineKeyboardButton('First words', callback_data='first_words')
    markup = types.InlineKeyboardMarkup()
    markup.add(item1)
    await callback.message.answer('ты конч', reply_markup=markup)
#-----------------------------------------------------------------------------------------------------------------------


async def first_words(callback: types.CallbackQuery):
    await bot.send_message(callback.message.chat.id,'this item has 4 wheels')
    await crocodile_game.first_message.set()

async def first_words_crocodile_game(message: types.Message, state: FSMContext):
    if message.text == "quad bike":
        await true_words(message)
        await state.finish()
    else:
        await bot.send_message(message.chat.id,'You can drive without a license')
        await crocodile_game.first_words_crocodile_game2.set()

async def first_words_crocodile_game2(message: types.Message, state: FSMContext):
    if message.text == "quad bike":
        await true_words(message)
        await state.finish()
    else:
        await bot.send_message(message.chat.id,'8 letters and two words')
        await crocodile_game.first_words_crocodile_game3.set()

async def first_words_crocodile_game3(message: types.Message, state: FSMContext):
    if message.text == "quad bike":
        await true_words(message)
        await state.finish()
    else:
        await bot.send_message(message.chat.id,'quad bike')
        await false_words(message)
        await state.finish()

async def true_words(message: types.Message):
    item1 = types.InlineKeyboardButton('⬅ Back', callback_data='back_menu')
    markup = types.InlineKeyboardMarkup()
    markup.add(item1)
    await message.answer('Congratulations you guessed the word!', reply_markup=markup)

async def false_words(message: types.Message):
    item1 = types.InlineKeyboardButton('⬅ Back', callback_data='back_menu')
    markup = types.InlineKeyboardMarkup()
    markup.add(item1)
    await message.answer('Unfortunately you didnt guess', reply_markup=markup)


# ----------------------------------------------------------------------------------------------------------------------


# Register hendlers-----------------------------------------------------------------------------------------------------
def expanded_game_f(dp: Dispatcher):
    dp.register_callback_query_handler(game_menu, text='game_menu')
    dp.register_callback_query_handler(word_game, text='word_game')
    dp.register_callback_query_handler(first_word_user_words_game, text='first_word_user_words_game')
    dp.register_callback_query_handler(crocodile_gamee, text='crocodile')
    dp.register_message_handler(first_word_bot_words_game, state=words_game.first_word_user)
    dp.register_message_handler(main_words_game, state=words_game.first_word_bot)
    dp.register_message_handler(first_words_crocodile_game, state=crocodile_game.first_message)
    dp.register_message_handler(first_words_crocodile_game2, state=crocodile_game.first_words_crocodile_game2)
    dp.register_message_handler(first_words_crocodile_game3, state=crocodile_game.first_words_crocodile_game3)
    dp.register_callback_query_handler(first_words, text='first_words')
#--------------------------------