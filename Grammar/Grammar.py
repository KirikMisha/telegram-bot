# from telebot import types
# from telebot import TeleBot
# from config import BOT_TOKEN
# bot = TeleBot(BOT_TOKEN)
#
# def Grammar(message):
#     markup = types.ReplyKeyboardMarkup()
#     item1 = types.KeyboardButton('🕰️ Time')
#     item2 = types.KeyboardButton('👮‍♂ Rules')
#     item3 = types.KeyboardButton('⬅ Back')
#     markup.add(item1, item2, item3)
#     bot.send_message(message.chat.id, 'описание граматики', reply_markup=markup)
#
# def Time(message):
#     markup = types.ReplyKeyboardMarkup()
#     item1 = types.KeyboardButton('⏳Present simple', )
#     item2 = types.KeyboardButton('⌚Present continuous')
#     item3 = types.KeyboardButton('⏰Present perfect')
#     item4 = types.KeyboardButton('🔞Past simple')
#     item5 = types.KeyboardButton('⬅ Back')
#     markup.add(item1, item2, item3, item4, item5)
#     bot.send_message(message.chat.id, 'описание граматики', reply_markup=markup)
# def Present_simple(message):
#     markup = types.ReplyKeyboardMarkup()
#     item1 = types.KeyboardButton('🙈TestFirst')
#     item2 = types.KeyboardButton('⬅ Back')
#     markup.add(item1, item2)
#     bot.send_photo(message.chat.id, "http://lingvana.ru/wp-content/uploads/2014/03/Tablitsa-past-simpl-skan.png", reply_markup=markup)
# def Present_continuous(message):
#     markup = types.ReplyKeyboardMarkup()
#     item1 = types.KeyboardButton('🙈TestSecond')
#     item2 = types.KeyboardButton('⬅ Back')
#     markup.add(item1, item2)
#     bot.send_photo(message.chat.id, "https://preply.com/wp-content/uploads/2018/04/Tablitsa-prezent-kontinius-2.jpg", reply_markup=markup)
# def Present_perfect(message):
#     pass