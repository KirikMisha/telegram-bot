# from telebot import types
# from telebot import TeleBot
# from config import BOT_TOKEN
# import random
#
# bot = TeleBot(BOT_TOKEN)
#
# def Game(message):
#     markup = types.ReplyKeyboardMarkup()
#     item1 = types.KeyboardButton('🐊 Crocodile')
#     item2 = types.KeyboardButton('Word Game')
#     item3 = types.KeyboardButton('⬅ Back')
#     markup.add(item1, item2, item3)
#     bot.send_message(message.chat.id, 'описание раздела игр', reply_markup=markup)
#
# # def game_word(message):
# #     str = message.text[-1].upper()
# #     with open(f'./Game/Words_to_words_game/{str}.txt', encoding='utf-8') as inp:
# #         letter = inp.readlines()
# #     i = random.randint(1, len(letter))
# #     msg = bot.send_message(message.chat.id, letter[i])
# #     bot.register_next_step_handler(msg, game_word)
#
#
# # def word_game(message):
# #     rmk = types.ReplyKeyboardMarkup()
# #     rmk.add(types.KeyboardButton("Да"), types.KeyboardButton("Нет"))
# #
# #     msg = bot.send_message(message.chat.id, "это игра в слова, хочешь продолжить?", reply_markup=rmk)
# #     bot.register_next_step_handler(msg, start_word_game)
#
# # def start_word_game(message):
# #     if message.text == "Нет":
# #         Game(message)
# #     elif message.text == "Да":
# #         msg = bot.send_message(message.chat.id, "Тогда начинай, твой ход")
# #         bot.register_next_step_handler(msg, game_word)
# #     else:
# #         bot.send_message(message.chat.id, 'Так не пойдет')