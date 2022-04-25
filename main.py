# from telebot import types
# from Game.Game import *
# from Grammar.Grammar import Grammar, Time, Present_simple, Present_continuous, Present_perfect
# from Vocabulary.Words import ordinary_words, number_ordinary_words, Irregular_verbs, Word, Basic_stable_expressions, \
#     Restart_ordinary_words, Restart_Basic_stable_expressions, Restart_Irregular_verbs, number_Irregular_verbs, \
#     number_Basic_stable_expressions
# from Links.Links import Links
# from db import Base
from config import *
from aiogram.utils import executor


from handlers import comands

comands.menu_hendlers(dp)








# # Создание новой строки в таблице базы данных по id пользователя
# @bot.message_handler(commands=['start'])
# def send_start(message):
#     Base(message)   # db
# # --------------------------------------------------------------------
#
# # Главное меню
# @bot.message_handler(commands=['menu'])
# def send_menu(message):
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     item1 = types.KeyboardButton('🕹️ Game')
#     item2 = types.KeyboardButton('📝 Grammar')
#     item3 = types.KeyboardButton('📚 Vocabulary')
#     item4 = types.KeyboardButton('Полезные ссылки')
#     markup.add(item1, item2, item3, item4)
#     bot.send_message(message.chat.id, '🗂️ Menu', reply_markup=markup)
# # --------------------------------------------------------------------
#
# from handlers  import Menu
#
#
#
#
#
#
#
#
# @bot.message_handler(content_types=['text'])
# def base(message):
#     if message.text == '🕹️ Game':
#         Game(message)
#
#     elif message.text == 'Word Game':
#         word_game(message)
#
#     elif message.text == '📝 Grammar':
#         Grammar(message)
#
#     elif message.text == '📚 Vocabulary':
#         Word(message)
#
#     elif message.text == '📚 Ordinary words':
#         ordinary_words(message)
#
#     elif message.text == '📖 Irregular verbs':
#         Irregular_verbs(message)
#
#     elif message.text == '💁‍♂ Basic stable expressions':
#         Basic_stable_expressions(message)
#
#     elif message.text == '📙 Restart':
#         Restart_Basic_stable_expressions(message)
#
#     elif message.text[0] == '📙':
#         number_Basic_stable_expressions(message)
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
#     elif message.text == 'Полезные ссылки':
#         Links(message)
#
#     elif message.text == '🕰️ Time':
#         Time(message)
#
#     elif message.text == '⬅ Back':
#         send_menu(message)
#
#     elif message.text == '⏳Present simple':
#         Present_simple(message)
#
#     elif message.text == '⌚Present continuous':
#         Present_continuous(message)
#
#     elif message.text == '⏰Present perfect':
#         Present_perfect(message)
#
#     elif message.text == '🔞Past simple':
#         markup = types.ReplyKeyboardMarkup()
#         item1 = types.KeyboardButton('🙈TestFourth')
#         item2 = types.KeyboardButton('⬅ Back')
#         markup.add(item1, item2)
#         bot.send_photo(message.chat.id, "http://grammar-tei.com/wp-content/uploads/2016/10/shema.jpg",
#                        reply_markup=markup)
#
#     elif message.text == '🙈TestFourth':
#         markup = types.ReplyKeyboardMarkup()
#         item1 = types.KeyboardButton('invited')  # Правильный ответ
#         item2 = types.KeyboardButton('invite')
#         item3 = types.KeyboardButton('inviting')
#         item4 = types.KeyboardButton('⬅ Back')
#         markup.add(item1, item2, item3, item4)
#         bot.send_message(message.chat.id, 'I (to invite) __ your friend to the party.', reply_markup=markup)
#
#     elif message.text == 'invited':
#         TrueAnswer += 1
#         bot.send_message(message.chat.id, 'True answer, my congratulation')
#
#     elif message.text == 'invited' or message.text == 'invite' or message.text == 'inviting':
#         markup = types.ReplyKeyboardMarkup()
#         item1 = types.KeyboardButton('found')  # True answer
#         item2 = types.KeyboardButton('finds')
#         item3 = types.KeyboardButton('finded')
#         item4 = types.KeyboardButton('⬅ Back')
#         markup.add(item1, item2, item3, item4)
#         bot.send_message(message.chat.id, 'Paul (to find) __ a good and inexpensive hotel.', reply_markup=markup)
#
#     elif message.text == 'found':
#         TrueAnswer += 1
#         bot.send_message(message.chat.id, 'True answer, my congratulation')
#
#
#
#
#
# def game_word(message):
#     str = message.text[-1].upper()
#     with open(f'./Game/Words_to_words_game/{str}.txt', encoding='utf-8') as inp:
#         letter = inp.readlines()
#     i = random.randint(1, len(letter))
#     msg = bot.send_message(message.chat.id, letter[i])
#     bot.register_next_step_handler(msg, game_word)
#
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
#
#
# bot.polling(none_stop=True)
executor.start_polling(dp, skip_updates=True)
