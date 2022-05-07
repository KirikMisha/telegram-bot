from config import bot, Dispatcher, test
from aiogram.dispatcher import FSMContext
from aiogram import types
import random


# Развертка меню игр----------------------------------------------------------------------------------------------------
async def game_menu(callback: types.CallbackQuery):
    await bot.delete_message(callback.from_user.id,callback.message.message_id)
    item1 = types.InlineKeyboardButton('🐊 Crocodile', callback_data='crocodile')
    item2 = types.InlineKeyboardButton('Word Game', callback_data='word_game')
    item3 = types.InlineKeyboardButton('⬅ Back to menu', callback_data='back_menu')
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(item1, item2, item3)
    await callback.message.answer('описание раздела игр', reply_markup=markup)
#-----------------------------------------------------------------------------------------------------------------------


# Игра в слова----------------------------------------------------------------------------------------------------------
async def word_game(callback: types.CallbackQuery):
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    item1 = types.InlineKeyboardButton('Да, поехали', callback_data='heaad_word_game')
    item2 = types.InlineKeyboardButton('⬅ Back to menu', callback_data='back_menu')
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(item1, item2)
    await callback.message.answer('Привет, это меню инры в слова, правила...\n'
                                  'Ты согласен продолжить, или вернешься назад?', reply_markup=markup)


async def head_word_game(callback: types.CallbackQuery):
    await bot.send_message(callback.message.chat.id, 'Ну если ты согласен, тогда начинай. \n'
                                                     'p.s(просто напиши любое слово из английского языка)')
    await test.test1.set()


async def start_words_game(message: types.Message, state: FSMContext):
    str = message.text[-1].upper()
    with open(f'./Game/Words_to_words_game/{str}.txt', encoding='utf-8') as inp:
        letter = inp.readlines()
    i = random.randint(1, len(letter))
    str1 = letter[i].split('\t')
    str1[0] = str1[0][-1]
    await bot.send_message(message.chat.id, letter[i])
    await bot.send_message(message.chat.id, f'Твоя очередь, слово должно начинатся на <b><u>{str1[0]}</u></b>'
                                            f'', parse_mode='html')
    # await state.update_data(test1=str1)
    await test.test2.set()


# async def body_words_game(message: types.Message, state: FSMContext):
#     await bot.send_message(message.chat.id, str1)





    # # def game_word(message):
    # #     str = message.text[-1].upper()
    #     with open(f'./Game/Words_to_words_game/{str}.txt', encoding='utf-8') as inp:
    #         letter = inp.readlines()
    #     i = random.randint(1, len(letter))
    #     msg = bot.send_message(message.chat.id, letter[i])
    #     bot.register_next_step_handler(msg, game_word)
    # #
    # def word_game(message):
    #     rmk = types.ReplyKeyboardMarkup()
    #     rmk.add(types.KeyboardButton("Да"), types.KeyboardButton("Нет"))
    #
    #     msg = bot.send_message(message.chat.id, "это игра в слова, хочешь продолжить?", reply_markup=rmk)
    #     bot.register_next_step_handler(msg, start_word_game)
    #
    # def start_word_game(message):
    #     if message.text == "Нет":
    #         Game(message)
    #     elif message.text == "Да":
    #         msg = bot.send_message(message.chat.id, "Тогда начинай, твой ход")
    #         bot.register_next_step_handler(msg, game_word)
    #     else:
    #         bot.send_message(message.chat.id, 'Так не пойдет')
#-----------------------------------------------------------------------------------------------------------------------


# Развертка игры крокодила----------------------------------------------------------------------------------------------
async def crocodile_game(callback: types.CallbackQuery):
    pass
#-----------------------------------------------------------------------------------------------------------------------


#Развертка граматики----------------------------------------------------------------------------------------------------
#     # elif message.text == '📝 Grammar':
#     #     item1 = types.KeyboardButton('🕰️ Time')
#     #     item2 = types.KeyboardButton('👮‍♂ Rules')
#     #     item3 = types.KeyboardButton('⬅ Back to menu')
#     #     markup = types.ReplyKeyboardMarkup()
#     #     markup.add(item1, item2, item3)
#     #     await bot.send_message(message.chat.id, 'описание граматики', reply_markup=markup)
#
#     elif message.text == '🕰️ Time':
#         item1 = types.KeyboardButton('⏳Present simple')
#         item2 = types.KeyboardButton('⌚Present continuous')
#         item3 = types.KeyboardButton('⏰Present perfect')
#         item4 = types.KeyboardButton('🔞Past simple')
#         item5 = types.KeyboardButton('⬅ Back to menu')
#         markup = types.ReplyKeyboardMarkup()
#         markup.add(item1, item2, item3, item4, item5)
#         await bot.send_message(message.chat.id, 'описание времени', reply_markup=markup)
#
#     elif message.text == '👮‍♂ Rules':
#         item1 = types.KeyboardButton('1')
#         item2 = types.KeyboardButton('2')
#         item3 = types.KeyboardButton('3')
#         item4 = types.KeyboardButton('4')
#         item5 = types.KeyboardButton('⬅ Back to menu')
#         markup = types.ReplyKeyboardMarkup()
#         markup.add(item1, item2, item3, item4, item5)
#         await bot.send_message(message.chat.id, 'описание времени', reply_markup=markup)
# #---------------------------------------------------------------------------------------------------------------------
#
# #Развертка ссылок-----------------------------------------------------------------------------------------------------
#     elif message.text == 'Полезные ссылки':
#         bot.send_message(message.chat.id, 'Ссылки')
# #---------------------------------------------------------------------------------------------------------------------
#
#
# #Кнопка возврата в меню-----------------------------------------------------------------------------------------------
#     if message.text == '⬅ Back to menu':
#         await send_menu(message) #comand
# #---------------------------------------------------------------------------------------------------------------------


def expanded_game_f(dp: Dispatcher):
    dp.register_callback_query_handler(game_menu,text='game_menu')
    dp.register_callback_query_handler(word_game, text='word_game')
    dp.register_callback_query_handler(head_word_game, text='head_word_game')
    dp.register_callback_query_handler(crocodile_game, text='crocodile')
    dp.register_message_handler(start_words_game,state=test.test1)
    # dp.register_message_handler(body_words_game, state=test.test2)
