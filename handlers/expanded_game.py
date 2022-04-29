from config import bot, Dispatcher
from aiogram import types


# Развертка меню игр----------------------------------------------------------------------------------------------------
async def game_menu(callback: types.CallbackQuery):
    await bot.delete_message(callback.from_user.id,callback.message.message_id)
    item1 = types.InlineKeyboardButton('🐊 Crocodile', callback_data='I_crocodile')
    item2 = types.InlineKeyboardButton('Word Game', callback_data='I_word_Game')
    item3 = types.InlineKeyboardButton('⬅ Back to menu', callback_data='I_back_menu')
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(item1, item2, item3)
    await callback.message.answer('описание раздела игр', reply_markup=markup)
#-----------------------------------------------------------------------------------------------------------------------


# Игра в слова----------------------------------------------------------------------------------------------------------
async def word_game(callback: types.CallbackQuery):
    pass
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
    dp.register_callback_query_handler(game_menu,text='I_game_menu')
    dp.register_callback_query_handler(word_game, text='I_word_Game')
    dp.register_callback_query_handler(crocodile_game, text='I_crocodile')
