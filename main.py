from telebot import TeleBot

bot = TeleBot('5317464669:AAG5R6klT_cURjoo0wbbe07mGwtVBu66x6Y')
with open('./Wordss/words.txt', encoding='utf-8') as inp:
    words = inp.readline().split()

# with open('./Wordss/transcriptions.txt') as f:
#     transcriptions = f.readline().split()

with open('./Wordss/translation.txt', encoding='utf-8') as inp:
    translation = inp.read().split()

@bot.message_handler(commands=['start'])
def start(message):
        for i in range(len(words)):
            mess = f'{words[i]}  {translation[i]}'
            bot.send_message(message.chat.id, mess)

bot.polling(none_stop=True)