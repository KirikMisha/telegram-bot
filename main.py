from telebot import TeleBot

bot = TeleBot('5317464669:AAG5R6klT_cURjoo0wbbe07mGwtVBu66x6Y')


@bot.message_handler(commands=['start'])
def start(message):
    with open('./Wordss/words.txt') as inp:
        massiv = inp.read().split()
        for i in range(len(massiv)):
            mess = f'{massiv[i]} {massiv[1]}'
            bot.send_message(message.chat.id, mess )




bot.polling(none_stop=True)