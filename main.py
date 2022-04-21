from telebot import TeleBot

bot = TeleBot('5317464669:AAG5R6klT_cURjoo0wbbe07mGwtVBu66x6Y')
with open('./Wordss/words.txt', encoding='utf-8') as inp:
    words = inp.readlines()

with open('./Wordss/transcriptions.txt', encoding='utf-8') as inp:
    transcriptions = inp.readlines()

with open('./Wordss/translation.txt', encoding='utf-8') as inp:
    translation = inp.readlines()


# @bot.message_handler(commands=['start'])
# def start(message):
#     for i in range(len(words)):
#         mess = f'{words[i]} {transcriptions[i]} {translation[i]}'
#         bot.send_message(message.chat.id, mess)

@bot.message_handler()
def word(message):
    if message.text == "words":
        for i in range(len(words)):
            mess = f'{words[i]} {transcriptions[i]} {translation[i]}'
            bot.send_message(message.chat.id, mess)
    else:
        bot.send_message(message.chat.id, "я тебя не понимать")


bot.polling(none_stop=True)
