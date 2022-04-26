# from telebot import types
# from telebot import TeleBot
# from config import BOT_TOKEN
# from db import Restart_ordinary_words, Restart_Irregular_verbs, Restart_Basic_stable_expressions, Plass, PlassB, PlassI
#
#
# bot = TeleBot(BOT_TOKEN)
#
#
# with open('./Vocabulary/IrregularVerbs.txt', encoding='utf-8') as inp:
#     Iwords = inp.readlines()
#
# with open('./Vocabulary/Stable_expressions.txt', encoding='utf-8') as inp:
#     Bwords = inp.readlines()
# def number_ordinary_words(message):
#     if message.text.replace('📗 ', '').isdigit():
#         number = int(message.text.replace('📗 ', ''))
#         i = Plass(message,number)
#         number = i + number
#         while i < number:
#             i = i + 1
#             bot.send_message(message.chat.id, Owords[i])
#             if i == 1415:
#                 bot.send_message(message.chat.id, 'Молодец, ты выучил весь Английский )')
#                 bot.send_photo(message.chat.id,'http://risovach.ru/upload/2014/03/mem/forever-alone_46449071_orig_.jpg')
#                 Restart_ordinary_words(message)
#                 break
#     else:
#         bot.send_message(message.chat.id, 'Enter a number\n'
#                                           'Example:📗 [number]')
#
# def number_Irregular_verbs(message):
#     if message.text.replace('📕 ', '').isdigit():
#         number = int(message.text.replace('📕 ', ''))
#         i = PlassI(message, number)
#         number = i + number
#         while i < number:
#             i = i + 1
#             bot.send_message(message.chat.id, Iwords[i])
#             if i == 119:
#                 bot.send_message(message.chat.id, 'Молодец, ты выучил весь Английский )')
#                 bot.send_photo(message.chat.id, 'http://risovach.ru/upload/2014/03/mem/forever-alone_46449071_orig_.jpg')
#                 Restart_Irregular_verbs(message)
#                 break
#     else:
#         bot.send_message(message.chat.id, 'Enter a number\n'
#                                           'Example:📗 [number]')
#
# def number_Basic_stable_expressions(message):
#     if message.text.replace('📙 ', '').isdigit():
#         number = int(message.text.replace('📙 ', ''))
#         i = PlassB(message, number)
#         number = i + number
#         while i < number:
#             i = i + 1
#             bot.send_message(message.chat.id, Bwords[i])
#             if i == 111:
#                 bot.send_message(message.chat.id, 'Молодец, ты выучил весь Английский )')
#                 bot.send_photo(message.chat.id, 'http://risovach.ru/upload/2014/03/mem/forever-alone_46449071_orig_.jpg')
#                 Restart_Basic_stable_expressions(message)
#                 break
#     else:
#         bot.send_message(message.chat.id, 'Enter a number\n'
#                                           'Example:📗 [number]')