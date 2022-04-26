from config import bot, Dispatcher
from aiogram import types

from db import Base


# Создание новой строки в таблице базы данных по id пользователя--------------
async def send_start(message: types.Message):
    await Base(message)  # db
# ----------------------------------------------------------------------------


# Вывод главного меню---------------------------------------------------------
async def send_menu(message: types.Message):
    item1 = types.KeyboardButton('🕹️ Game')
    item2 = types.KeyboardButton('📝 Grammar')
    item3 = types.KeyboardButton('📚 Vocabulary')
    item4 = types.KeyboardButton('Полезные ссылки')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    markup.add(item1, item2, item3, item4)
    await bot.send_message(message.chat.id, '🗂️ Menu', reply_markup=markup)
#-----------------------------------------------------------------------------


def menu_hendlers(dp: Dispatcher):
    dp.register_message_handler(send_menu, commands=['menu'])
    dp.register_message_handler(send_start, commands=['start'])
