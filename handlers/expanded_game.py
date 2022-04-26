from config import bot, Dispatcher
from aiogram import types


#Развертка меню игр-----------------------------------------------------------------------------------------------------
async def Game(message: types.Message):
    item1 = types.KeyboardButton('🐊 Crocodile')
    item2 = types.KeyboardButton('Word Game')
    item3 = types.KeyboardButton('⬅ Back to menu')
    markup = types.ReplyKeyboardMarkup()
    markup.add(item1, item2, item3)
    await bot.send_message(message.chat.id, 'описание раздела игр', reply_markup=markup)
#-----------------------------------------------------------------------------------------------------------------------


#Игра в слова-----------------------------------------------------------------------------------------------------------
async def word_game(message: types.Message):
    pass
#-----------------------------------------------------------------------------------------------------------------------


#Развертка игр----------------------------------------------------------------------------------------------------------
async def crocodile(message: types.Message):
    pass
#-----------------------------------------------------------------------------------------------------------------------




# async def expanded_menu(message: types.Message):
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
# #-----------------------------------------------------------------------------------------------------------------------
#
#
# #Развертка строк--------------------------------------------------------------------------------------------------------
#
#     elif message.text == '📖 Irregular verbs':
#         item1 = types.KeyboardButton('📕 1')
#         item2 = types.KeyboardButton('📕 3')
#         item3 = types.KeyboardButton('📕 5')
#         item4 = types.KeyboardButton('⬅ Back to menu')
#         markup = types.ReplyKeyboardMarkup()
#         markup.add(item1, item2, item3, item4)
#         await bot.send_message(message.chat.id, 'В этом разделе ты выберешь сколько неправильных глаголов я тебе '
#                                                 'выдам на заучивание сегодня.Оптимальным вариантом будет учить по 5-10 '
#                                                 'слов в день, однако главным в этом деле, учить хотя бы одно слово-это '
#                                                 'уже прогресс.\np.s. ( при выборе желаемого количества слов напиши в '
#                                                 'чат 📕 *пробел* цифра)p.p.s. (если хочешь начать с самого начала вбей '
#                                                 'команду: 📕 Restart)'
#                                                 '', reply_markup=markup)
#
#     elif message.text == '💁‍♂ Basic stable expressions':
#         item1 = types.KeyboardButton('📙 1')
#         item2 = types.KeyboardButton('📙 3')
#         item3 = types.KeyboardButton('📙 5')
#         item4 = types.KeyboardButton('⬅ Back to menu')
#         markup = types.ReplyKeyboardMarkup()
#         markup.add(item1, item2, item3, item4)
#         await bot.send_message(message.chat.id, 'В этом разделе ты выберешь сколько базовых устойчивых выражений '
#                                                 'английского языка я тебе выдам на заучивание сегодня.Оптимальным '
#                                                 'вариантом будет учить по 5-10 слов в день, однако главным в этом '
#                                                 'деле, учить хотя бы одно слово-это уже прогресс.\np.s. ( при выборе '
#                                                 'желаемого количества слов напиши в чат 📙 *пробел* цифра)p.p.s. (если '
#                                                 'хочешь начать с самого начала вбей команду: 📙 Restart)'
#                                                 '', reply_markup=markup)
# #-----------------------------------------------------------------------------------------------------------------------
#
#
# #Развертка ссылок-------------------------------------------------------------------------------------------------------
#     elif message.text == 'Полезные ссылки':
#         bot.send_message(message.chat.id, 'Ссылки')
# #-----------------------------------------------------------------------------------------------------------------------
#
#
# #Кнопка возврата в меню-------------------------------------------------------------------------------------------------
#     if message.text == '⬅ Back to menu':
#         await send_menu(message) #comand
# #-----------------------------------------------------------------------------------------------------------------------


def expanded_menu_hendlers(dp: Dispatcher):
    dp.register_callback_query_handler(Game,text='🕹️ Game')
