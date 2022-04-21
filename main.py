from telebot import TeleBot;

bot = TeleBot('5317464669:AAG5R6klT_cURjoo0wbbe07mGwtVBu66x6Y')


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет, <b>{message.from_user.first_name} {message.from_user.last_name}</b>'
    bot.send_message(message.chat.id, mess, parse_mode='html')

@bot.message_handler()
def get_user_text(message):
    bot.send_message(message.chat.id, message, parse_mode='html')


bot.polling(none_stop=True)
