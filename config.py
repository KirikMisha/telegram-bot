from aiogram.dispatcher import Dispatcher
from aiogram import Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage

bot = Bot('5317464669:AAG5R6klT_cURjoo0wbbe07mGwtVBu66x6Y')
dp = Dispatcher(bot, storage=MemoryStorage())

from aiogram.dispatcher.filters.state import StatesGroup, State


class words_game(StatesGroup):
    first_word_user = State()
    first_word_bot = State()

class test(StatesGroup):
    test1 = State()
    test2 = State()



