from config import bot, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, Message, ReplyKeyboardMarkup, \
    KeyboardButton
from aiogram.dispatcher import filters
from config import test
from aiogram.dispatcher import FSMContext

async def grammar_menu(callback: CallbackQuery):
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    item1 = InlineKeyboardButton('🕰️ Time', callback_data='time')
    item2 = InlineKeyboardButton('👮‍♂ Rules',callback_data='time')
    item3 = InlineKeyboardButton('⬅ Back',callback_data='back_menu')
    markup = InlineKeyboardMarkup(row_width=2)
    markup.add(item1, item2, item3)
    await callback.message.answer('описание граматики', reply_markup=markup)

async def time(callback: CallbackQuery):
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    item1 = InlineKeyboardButton('⏳Present simple', callback_data='present_simple')
    item2 = InlineKeyboardButton('⌚Present continuous',callback_data='present_continuous')
    item3 = InlineKeyboardButton('⏰Present perfect',callback_data='present_perfect')
    item4 = InlineKeyboardButton('🔞Past simple',callback_data='past_simple')
    item5 = InlineKeyboardButton('⬅ Back',callback_data='back_menu')
    markup = InlineKeyboardMarkup()
    markup.add(item1, item2, item3, item4, item5)
    await callback.message.answer('описание граматики', reply_markup=markup)


async def present_simple(callback: CallbackQuery):
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    item1 = InlineKeyboardButton('🙈TestFirst', callback_data='test_first_simple')
    item2 = InlineKeyboardButton('⬅ Back', callback_data='back_menu')
    markup = InlineKeyboardMarkup()
    markup.add(item1, item2)
    await callback.message.answer("http://lingvana.ru/wp-content/uploads/2014/03/Tablitsa-past-simpl-skan.png", reply_markup=markup)
async def present_continuous(callback: CallbackQuery):
    item1 = InlineKeyboardButton('🙈TestSecond', callback_data='time')
    item2 = InlineKeyboardButton('⬅ Back', callback_data='back_menu')
    markup = InlineKeyboardMarkup()
    markup.add(item1, item2)
    await callback.message.answer("https://preply.com/wp-content/uploads/2018/04/Tablitsa-prezent-kontinius-2.jpg", reply_markup=markup)
async def present_perfect(callback: CallbackQuery):
    item1 = InlineKeyboardButton('🙈TestЕhird', callback_data='time')
    item2 = InlineKeyboardButton('⬅ Back', callback_data='back_menu')
    markup = InlineKeyboardMarkup()
    markup.add(item1, item2)
    await callback.message.answer("https://lingvana.ru/wp-content/uploads/2014/02/Prezent-perfekt-tablitsa.png", reply_markup=markup)
async def past_simple(callback: CallbackQuery):
    item1 = InlineKeyboardButton('🙈TestFourth', callback_data='time')
    item2 = InlineKeyboardButton('⬅ Back', callback_data='back_menu')
    markup = InlineKeyboardMarkup()
    markup.add(item1, item2)
    await callback.message.answer("http://grammar-tei.com/wp-content/uploads/2016/10/shema.jpg", reply_markup=markup)

#Test Simple-------------------------------------------------------------------------------------------------------------------------
async def test_first_simple(callback: CallbackQuery):
    item1 = KeyboardButton('invited')  # Правильный ответ
    item2 = KeyboardButton('invite')
    item3 = KeyboardButton('inviting')
    markup = ReplyKeyboardMarkup()
    markup.add(item1, item2, item3)
    await callback.message.answer('I (to invite) __ your friend to the party.', reply_markup=markup)
    await test.test1.set()


async def test2_simple(message: Message, state: FSMContext):
    if message.text == 'invited':
        await bot.send_message(message.chat.id, 'ответ верный')
    else:
        await bot.send_message(message.chat.id, 'ответ не верный, правильный ответ: invited')
    item1 = KeyboardButton('found')  # True answer
    item2 = KeyboardButton('finds')
    item3 = KeyboardButton('finded')
    markup = ReplyKeyboardMarkup()
    markup.add(item1, item2, item3)
    await message.answer( 'Paul (to find) __ a good and inexpensive hotel.', reply_markup=markup)
    await test.test2.set()
    # await state.finish()-----------=========


async def test3_simple(message: Message, state: FSMContext):
    markup = ReplyKeyboardMarkup()
    item1 = KeyboardButton('understanded')
    item2 = KeyboardButton('understand')
    item3 = KeyboardButton('understood')   # Правильный ответ
    markup.add(item1, item2, item3)
    await bot.send_message(message.chat.id, 'We (to understand) __ each other..', reply_markup=markup)

# def Test4_simple(message):
#     markup = types.ReplyKeyboardMarkup()
#     item1 = types.KeyboardButton('... didn’t play chess yesterday.') # Правильный ответ
#     item2 = types.KeyboardButton('... did no play chess yesterday.')
#     item3 = types.KeyboardButton('... not played chess yesterday.')
#     item4 = types.KeyboardButton('⬅ Back')
#     markup.add(item1, item2, item3, item4)
#     bot.send_message(message.chat.id, 'В каком варианте представлена отрицательная форма данного предложения: «Billy and Jim played chess yesterday»?', reply_markup=markup)
# def Test5_simple(message):
#     markup = types.ReplyKeyboardMarkup()
#     item1 = types.KeyboardButton('had')
#     item2 = types.KeyboardButton('did sang')  # Правильный ответ
#     item3 = types.KeyboardButton('didn’t say')
#     item4 = types.KeyboardButton('⬅ Back')
#     markup.add(item1, item2, item3, item4)
#     bot.send_message(message.chat.id, ' В каком варианте ответа допущена ошибка?', reply_markup=markup)
# def Test6_simple(message):
#     markup = types.ReplyKeyboardMarkup()
#     item1 = types.KeyboardButton('had.')   # Правильный ответ
#     item2 = types.KeyboardButton('did have')
#     item3 = types.KeyboardButton('did')
#     item4 = types.KeyboardButton('⬅ Back')
#     markup.add(item1, item2, item3, item4)
#     bot.send_message(message.chat.id, ' Дополните предложение “Andy … an interesting idea”, используя подходящую форму глагола:', reply_markup=markup)
# def Test7_simple(massage):
#     markup = types.ReplyKeyboardMarkup()
#     item1 = types.KeyboardButton('She not looked alive.')  # Правильный ответ
#     item2 = types.KeyboardButton('The man introduced me to his wife last week.')
#     item3 = types.KeyboardButton('Yesterday I was getting very worried.')
#     item4 = types.KeyboardButton('⬅ Back')
#     markup.add(item1, item2, item3, item4)
#     bot.send_message(message.chat.id, ' Найдите предложение, в котором допущена ошибка:', reply_markup=markup)
# def Test8_simple(message):
#     markup = types.ReplyKeyboardMarkup()
#     bot.send_message(message.chat.id, ' 1)Masha didn’t like his behavior.', reply_markup=markup)
#     bot.send_message(message.chat.id, ' 2)TDid Ann clean her room yesterday?', reply_markup=markup)
#     bot.send_message(message.chat.id, ' 3)When did you buy those boots?', reply_markup=markup)
#     item1 = types.KeyboardButton('1')
#     item2 = types.KeyboardButton('2')
#     item3 = types.KeyboardButton('3')  # Правильный ответ
#     item4 = types.KeyboardButton('⬅ Back')
#     markup.add(item1, item2, item3, item4)
#     bot.send_message(message.chat.id, ' В каком предложении употреблен неправильный глагол?', reply_markup=markup)
# def Test9_simple(message):
#     markup = types.ReplyKeyboardMarkup()
#     item1 = types.KeyboardButton('did go')
#     item2 = types.KeyboardButton('go')  # Правильный ответ
#     item3 = types.KeyboardButton('gone')
#     item4 = types.KeyboardButton('⬅ Back')
#     markup.add(item1, item2, item3, item4)
#     bot.send_message(message.chat.id, 'Дополните предложение “Where did everybody … yesterday?”, используя подходящую форму глагола:', reply_markup=markup)

# Register hendlers-----------------------------------------------------------------------------------------------------
def expanded_grammar_f(dp: Dispatcher):
    dp.register_callback_query_handler(grammar_menu, text='grammar_menu')
    dp.register_callback_query_handler(time, text='time')
    dp.register_callback_query_handler(present_simple, text='present_simple')
    dp.register_callback_query_handler(present_continuous, text='present_continuous')
    dp.register_callback_query_handler(present_perfect, text='present_perfect')
    dp.register_callback_query_handler(past_simple, text='past_simple')
    dp.register_callback_query_handler(test_first_simple, text='test_first_simple')
    dp.register_message_handler(test2_simple, state=test.test1)
    dp.register_message_handler(test3_simple, state=test.test2)

# -----------------------------------------------------------------------------------------------------------------------
