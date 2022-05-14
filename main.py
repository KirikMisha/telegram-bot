from config import dp
from aiogram.utils import executor

from handlers import comands
from handlers import expanded_game
from handlers import expanded_vocabluary
from handlers import expanded_links
from handlers import expanded_grammar

comands.menu_hendlers(dp)
expanded_game.expanded_game_f(dp)
expanded_vocabluary.expanded_vocabulary_f(dp)
expanded_grammar.expanded_grammar_f(dp)
expanded_links.expanded_links_f(dp)


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

executor.start_polling(dp, skip_updates=True)
