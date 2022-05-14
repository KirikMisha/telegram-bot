from config import bot, Dispatcher,dp
from aiogram import types

from db import Base


# Создание новой строки в таблице базы данных по id пользователя--------------------------------------------------------
async def send_start(message: types.Message):
    await Base(message)  # db
    # dp.send_message(message.chat.id, 'Привет, я бот помошник в изучении Английского')
# ----------------------------------------------------------------------------------------------------------------------


# Вывод главного меню---------------------------------------------------------------------------------------------------
async def send_menu(message: types.Message):
    item1 = types.InlineKeyboardButton('🕹️ Game', callback_data='game_menu')
    item2 = types.InlineKeyboardButton('📝 Grammar', callback_data='grammar_menu')
    item3 = types.InlineKeyboardButton('📚 Vocabulary', callback_data='vocabulary_menu')
    item4 = types.InlineKeyboardButton('Полезные ссылки', callback_data='links_menu')
    markup = types.InlineKeyboardMarkup()
    markup.add(item1, item2, item3, item4)
    await message.answer('🗂️ Menu', reply_markup=markup)
#-----------------------------------------------------------------------------------------------------------------------

# Возврат в главное меню------------------------------------------------------------------------------------------------
async def back(callback: types.CallbackQuery):
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    await send_menu(callback.message)
#-----------------------------------------------------------------------------------------------------------------------


def menu_hendlers(dp: Dispatcher):
    dp.register_message_handler(send_menu, commands=['menu'])
    dp.register_message_handler(send_start, commands=['start'])
    dp.register_callback_query_handler(back, text='back_menu')