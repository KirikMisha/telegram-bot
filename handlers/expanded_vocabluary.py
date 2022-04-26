from config import bot, Dispatcher,dp
from aiogram import types

# @dp.callback_query_handlers(text='📚 Vocabulary')
async def vocabulary(message: types.Message):
    item1 = types.KeyboardButton('📚 Ordinary words')
    item2 = types.KeyboardButton('📖 Irregular verbs')
    item3 = types.KeyboardButton('💁‍♂ Basic stable expressions')
    item4 = types.KeyboardButton('⬅ Back to menu')
    markup = types.ReplyKeyboardMarkup()
    markup.add(item1, item2, item3, item4)
    await bot.send_message(message.chat.id, 'описание слов', reply_markup=markup)

async def ordinary_words(message: types.Message):
    item1 = types.KeyboardButton('📗 1')
    item2 = types.KeyboardButton('📗 5')
    item3 = types.KeyboardButton('📗 10')
    item4 = types.KeyboardButton('⬅ Back to menu')
    markup = types.ReplyKeyboardMarkup()
    markup.add(item1, item2, item3, item4)
    await bot.send_message(message.chat.id, 'В этом разделе ты выберешь сколько слов я тебе выдам на заучивание '
                                                'сегодня.Оптимальным вариантом будет учить по 5-10 слов в день, однако '
                                                'главным в этом деле, учить хотя бы одно слово-это уже прогресс.\n'
                                                'p.s. ( при выборе желаемого количества слов напиши в чат 📗 *пробел* '
                                                'цифра)\np.p.s. (если хочешь начать с самого начала вбей команду: 📗 '
                                                'Restart)'
                                                '', reply_markup=markup)





def expanded_vocabulary(dp: Dispatcher):
    dp.register_callback_query_handler(vocabulary,text='📚 Vocabulary')
    dp.register_callback_query_handler(ordinary_words, text='📚 Ordinary words')