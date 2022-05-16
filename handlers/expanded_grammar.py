from config import bot, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, Message, ReplyKeyboardMarkup, \
    KeyboardButton
from aiogram.dispatcher import filters
from config import test
from aiogram.dispatcher import FSMContext


async def grammar_menu(callback: CallbackQuery):
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    item1 = InlineKeyboardButton('🕰️ Time', callback_data='time')
    item2 = InlineKeyboardButton('👮‍♂ Rules', callback_data='time')
    item3 = InlineKeyboardButton('⬅ Back', callback_data='back_menu')
    markup = InlineKeyboardMarkup(row_width=2)
    markup.add(item1, item2, item3)
    await callback.message.answer('описание граматики', reply_markup=markup)


async def time(callback: CallbackQuery):
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    item1 = InlineKeyboardButton('⏳Present simple', callback_data='present_simple')
    item2 = InlineKeyboardButton('⌚Present continuous', callback_data='present_continuous')
    item3 = InlineKeyboardButton('⏰Present perfect', callback_data='present_perfect')
    item4 = InlineKeyboardButton('🔞Past simple', callback_data='past_simple')
    item5 = InlineKeyboardButton('⬅ Back', callback_data='back_menu')
    markup = InlineKeyboardMarkup()
    markup.add(item1, item2, item3, item4, item5)
    await callback.message.answer('описание граматики', reply_markup=markup)


async def present_simple(callback: CallbackQuery):
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    item1 = InlineKeyboardButton('🙈TestFirst', callback_data='test_first_simple')
    item2 = InlineKeyboardButton('⬅ Back', callback_data='back_menu')
    markup = InlineKeyboardMarkup()
    markup.add(item1, item2)
    await callback.message.answer("http://lingvana.ru/wp-content/uploads/2014/03/Tablitsa-past-simpl-skan.png",
                                  reply_markup=markup)


async def present_continuous(callback: CallbackQuery):
    item1 = InlineKeyboardButton('🙈TestSecond', callback_data='test_second_continuous')
    item2 = InlineKeyboardButton('⬅ Back', callback_data='back_menu')
    markup = InlineKeyboardMarkup()
    markup.add(item1, item2)
    await callback.message.answer("https://preply.com/wp-content/uploads/2018/04/Tablitsa-prezent-kontinius-2.jpg",
                                  reply_markup=markup)


async def present_perfect(callback: CallbackQuery):
    item1 = InlineKeyboardButton('🙈TestЕhird', callback_data='test_second_perfect')
    item2 = InlineKeyboardButton('⬅ Back', callback_data='back_menu')
    markup = InlineKeyboardMarkup()
    markup.add(item1, item2)
    await callback.message.answer("https://lingvana.ru/wp-content/uploads/2014/02/Prezent-perfekt-tablitsa.png",
                                  reply_markup=markup)


async def past_simple(callback: CallbackQuery):
    item1 = InlineKeyboardButton('🙈TestFourth', callback_data='test_second_past')
    item2 = InlineKeyboardButton('⬅ Back', callback_data='back_menu')
    markup = InlineKeyboardMarkup()
    markup.add(item1, item2)
    await callback.message.answer("http://grammar-tei.com/wp-content/uploads/2016/10/shema.jpg", reply_markup=markup)


# Test Simple-------------------------------------------------------------------------------------------------------------------------
async def test_first_simple(callback: CallbackQuery):
    item1 = KeyboardButton('invited')  # Правильный ответ
    item2 = KeyboardButton('invite')
    item3 = KeyboardButton('inviting')
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
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
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(item1, item2, item3)
    await message.answer('Paul (to find) __ a good and inexpensive hotel.', reply_markup=markup)
    await test.test2.set()


async def test3_simple(message: Message, state: FSMContext):
    if message.text == 'found':
        await bot.send_message(message.chat.id, 'ответ верный')
    else:
        await bot.send_message(message.chat.id, 'ответ не верный, правильный ответ: found')
    item1 = KeyboardButton('understanded')
    item2 = KeyboardButton('understand')
    item3 = KeyboardButton('understood')  # Правильный ответ
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(item1, item2, item3)
    await message.answer('We (to understand) __ each other..', reply_markup=markup)
    await test.test3.set()


async def test4_simple(message: Message, state: FSMContext):
    if message.text == 'understood':
        await bot.send_message(message.chat.id, 'ответ верный')
    else:
        await bot.send_message(message.chat.id, 'ответ не верный, правильный ответ: understood')
    item1 = KeyboardButton('... didn’t play chess yesterday.')  # Правильный ответ
    item2 = KeyboardButton('... did no play chess yesterday.')
    item3 = KeyboardButton('... not played chess yesterday.')
    markup = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    markup.add(item1, item2, item3)
    await message.answer('В каком варианте представлена отрицательная форма данного предложения: «Billy and Jim played'
                         ' chess yesterday»?', reply_markup=markup)
    await test.test4.set()


async def test5_simple(message: Message, state: FSMContext):
    if message.text == '... didn’t play chess yesterday.':
        await bot.send_message(message.chat.id, 'ответ верный')
    else:
        await bot.send_message(message.chat.id, 'ответ не верный, правильный ответ: ... didn’t play chess yesterday.')
    item1 = KeyboardButton('had')
    item2 = KeyboardButton('did sang')  # Правильный ответ
    item3 = KeyboardButton('didn’t say')
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(item1, item2, item3)
    await message.answer(' В каком варианте ответа допущена ошибка?', reply_markup=markup)
    await test.test5.set()


async def test6_simple(message: Message, state: FSMContext):
    if message.text == 'did sang':
        await bot.send_message(message.chat.id, 'ответ верный')
    else:
        await bot.send_message(message.chat.id, 'ответ не верный, правильный ответ: did sang')
    markup = InlineKeyboardMarkup(resize_keyboard=True)
    item1 = InlineKeyboardButton('⬅ Back', callback_data='back_menu')
    markup.add(item1)
    await message.answer('Поздравляю вы прошли тест!', reply_markup=markup)
    await state.finish()


# Test present continuous-----------------------------------------------------------------------------------------------

async def test_second_continuous(callback: CallbackQuery):
    item1 = KeyboardButton('am cooking')
    item2 = KeyboardButton('is cooking')  # Правильный ответ
    item3 = KeyboardButton('are cooking')
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(item1, item2, item3)
    await callback.message.answer('Where is Ann? She .... in the kitchen.', reply_markup=markup)
    await test.test6.set()


async def test2_continuous(message: Message, state: FSMContext):
    if message.text == 'is cooking':
        await bot.send_message(message.chat.id, 'ответ верный')
    else:
        await bot.send_message(message.chat.id, 'ответ не верный, правильный ответ: is cooking')
    item1 = KeyboardButton('walking')
    item2 = KeyboardButton('is walking')
    item3 = KeyboardButton('are walking')  # True answer
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(item1, item2, item3)
    await message.answer('They .... in the park now.', reply_markup=markup)
    await test.test7.set()


async def test3_continuous(message: Message, state: FSMContext):
    if message.text == 'are walking':
        await bot.send_message(message.chat.id, 'ответ верный')
    else:
        await bot.send_message(message.chat.id, 'ответ не верный, правильный ответ: are walking')
    item1 = KeyboardButton('is snows')
    item2 = KeyboardButton('are snows')
    item3 = KeyboardButton('are snowing')  # Правильный ответ
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(item1, item2, item3)
    await message.answer('Look! It .... heavily.', reply_markup=markup)
    await test.test8.set()


async def test4_continuous(message: Message, state: FSMContext):
    if message.text == 'are snows':
        await bot.send_message(message.chat.id, 'ответ верный')
    else:
        await bot.send_message(message.chat.id, 'ответ не верный, правильный ответ: are snows')
    item1 = KeyboardButton('fixes')
    item2 = KeyboardButton('fixing')
    item3 = KeyboardButton('is fixing')  # Правильный ответ
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(item1, item2, item3)
    await message.answer('Its Tom. He .... his car', reply_markup=markup)
    await test.test9.set()


async def test5_continuous(message: Message, state: FSMContext):
    if message.text == 'is fixing':
        await bot.send_message(message.chat.id, 'ответ верный')
    else:
        await bot.send_message(message.chat.id, 'ответ не верный, правильный ответ: is fixing')
    item1 = KeyboardButton('wait')
    item2 = KeyboardButton('is waiting')
    item3 = KeyboardButton('am waiting')  # Правильный ответ
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(item1, item2, item3)
    await message.answer(' I .... for you.', reply_markup=markup)
    await test.test10.set()


async def test6_continuous(message: Message, state: FSMContext):
    if message.text == 'am waiting':
        await bot.send_message(message.chat.id, 'ответ верный')
    else:
        await bot.send_message(message.chat.id, 'ответ не верный, правильный ответ: am waiting')
    markup = InlineKeyboardMarkup(resize_keyboard=True)
    item1 = InlineKeyboardButton('⬅ Back', callback_data='back_menu')
    markup.add(item1)
    await message.answer('Поздравляю вы прошли тест!', reply_markup=markup)
    await state.finish()


#present_perfect--------------------------------------------------------------------------------------------------------

async def test_second_perfect(callback: CallbackQuery):
    item1 = KeyboardButton('has broke')
    item2 = KeyboardButton('have broken')
    item3 = KeyboardButton('has broken') # Правильный ответ
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(item1, item2, item3)
    await callback.message.answer('My car .... down.', reply_markup=markup)
    await test.test11.set()


async def test2_perfect(message: Message, state: FSMContext):
    if message.text == 'has broken':
        await bot.send_message(message.chat.id, 'ответ верный')
    else:
        await bot.send_message(message.chat.id, 'ответ не верный, правильный ответ: has broken')
    item1 = KeyboardButton('have answered')     # True answer
    item2 = KeyboardButton('has answerd')
    item3 = KeyboardButton('have answeren')
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(item1, item2, item3)
    await message.answer('They .... all my questions.', reply_markup=markup)
    await test.test12.set()


async def test3_perfect(message: Message, state: FSMContext):
    if message.text == 'have answered':
        await bot.send_message(message.chat.id, 'ответ верный')
    else:
        await bot.send_message(message.chat.id, 'ответ не верный, правильный ответ: have answered')
    item1 = KeyboardButton('ve known')  # Правильный ответ
    item2 = KeyboardButton('has known')
    item3 = KeyboardButton('have knowen')
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(item1, item2, item3)
    await message.answer('I .... Nick for 10 years.', reply_markup=markup)
    await test.test13.set()


async def test4_perfect(message: Message, state: FSMContext):
    if message.text == 've known':
        await bot.send_message(message.chat.id, 'ответ верный')
    else:
        await bot.send_message(message.chat.id, 'ответ не верный, правильный ответ: ve known')
    item1 = KeyboardButton('have lost')
    item2 = KeyboardButton('has lose')
    item3 = KeyboardButton('has lost')  # Правильный ответ
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(item1, item2, item3)
    await message.answer('She .... her keys.', reply_markup=markup)
    await test.test14.set()


async def test5_perfect(message: Message, state: FSMContext):
    if message.text == 'has lost':
        await bot.send_message(message.chat.id, 'ответ верный')
    else:
        await bot.send_message(message.chat.id, 'ответ не верный, правильный ответ: has lost')
    item1 = KeyboardButton('have drunk')
    item2 = KeyboardButton('has drunk')     # Правильный ответ
    item3 = KeyboardButton('has drank')
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(item1, item2, item3)
    await message.answer('The cat .... all of its milk.', reply_markup=markup)
    await test.test15.set()


async def test6_perfect(message: Message, state: FSMContext):
    if message.text == 'has drunk':
        await bot.send_message(message.chat.id, 'ответ верный')
    else:
        await bot.send_message(message.chat.id, 'ответ не верный, правильный ответ: has drunk')
    markup = InlineKeyboardMarkup(resize_keyboard=True)
    item1 = InlineKeyboardButton('⬅ Back', callback_data='back_menu')
    markup.add(item1)
    await message.answer('Поздравляю вы прошли тест!', reply_markup=markup)
    await state.finish()


#past_simple------------------------------------------------------------------------------------------------------------


async def test_second_past(callback: CallbackQuery):
    item1 = KeyboardButton('come')
    item2 = KeyboardButton('came')  # Правильный ответ
    item3 = KeyboardButton('comed')
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(item1, item2, item3)
    await callback.message.answer('He .... home late last night.', reply_markup=markup)
    await test.test16.set()


async def test2_past(message: Message, state: FSMContext):
    if message.text == 'came':
        await bot.send_message(message.chat.id, 'ответ верный')
    else:
        await bot.send_message(message.chat.id, 'ответ не верный, правильный ответ: came')
    item1 = KeyboardButton('finishen')
    item2 = KeyboardButton('finish')
    item3 = KeyboardButton('finished')  # True answer
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(item1, item2, item3)
    await message.answer('She .... her work half an hour ago.', reply_markup=markup)
    await test.test17.set()


async def test3_past(message: Message, state: FSMContext):
    if message.text == 'have answered':
        await bot.send_message(message.chat.id, 'ответ верный')
    else:
        await bot.send_message(message.chat.id, 'ответ не верный, правильный ответ: have answered')
    item1 = KeyboardButton('saw')  # Правильный ответ
    item2 = KeyboardButton('see')
    item3 = KeyboardButton('seen')
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(item1, item2, item3)
    await message.answer('I .... this film last week.', reply_markup=markup)
    await test.test18.set()


async def test4_past(message: Message, state: FSMContext):
    if message.text == 'saw':
        await bot.send_message(message.chat.id, 'ответ верный')
    else:
        await bot.send_message(message.chat.id, 'ответ не верный, правильный ответ: saw')
    item1 = KeyboardButton('happen')
    item2 = KeyboardButton('happened')  # Правильный ответ
    item3 = KeyboardButton('happend')
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(item1, item2, item3)
    await message.answer('It .... on a sunny spring day.', reply_markup=markup)
    await test.test19.set()


async def test5_past(message: Message, state: FSMContext):
    if message.text == 'has lost':
        await bot.send_message(message.chat.id, 'ответ верный')
    else:
        await bot.send_message(message.chat.id, 'ответ не верный, правильный ответ: has lost')
    item1 = KeyboardButton('was')   # Правильный ответ
    item2 = KeyboardButton('were')
    item3 = KeyboardButton('been')
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(item1, item2, item3)
    await message.answer('I .... born in August.', reply_markup=markup)
    await test.test20.set()


async def test6_past(message: Message, state: FSMContext):
    if message.text == 'was':
        await bot.send_message(message.chat.id, 'ответ верный was')
    else:
        await bot.send_message(message.chat.id, 'ответ не верный, правильный ответ: has drunk')
    markup = InlineKeyboardMarkup(resize_keyboard=True)
    item1 = InlineKeyboardButton('⬅ Back', callback_data='back_menu')
    markup.add(item1)
    await message.answer('Поздравляю вы прошли тест!', reply_markup=markup)
    await state.finish()


# Register hendlers-----------------------------------------------------------------------------------------------------
def expanded_grammar_f(dp: Dispatcher):
    dp.register_callback_query_handler(grammar_menu, text='grammar_menu')
    dp.register_callback_query_handler(time, text='time')
    dp.register_callback_query_handler(present_simple, text='present_simple')
    dp.register_callback_query_handler(present_continuous, text='present_continuous')
    dp.register_callback_query_handler(present_perfect, text='present_perfect')
    dp.register_callback_query_handler(past_simple, text='past_simple')
    dp.register_callback_query_handler(test_first_simple, text='test_first_simple')
    dp.register_callback_query_handler(test_second_continuous, text='test_second_continuous')
    dp.register_callback_query_handler(test_second_perfect, text='test_second_perfect')
    dp.register_callback_query_handler(test_second_perfect, text='test_second_past')
    #--------
    dp.register_message_handler(test2_simple, state=test.test1)
    dp.register_message_handler(test3_simple, state=test.test2)
    dp.register_message_handler(test4_simple, state=test.test3)
    dp.register_message_handler(test5_simple, state=test.test4)
    dp.register_message_handler(test6_simple, state=test.test5)
    #---------
    dp.register_message_handler(test2_continuous, state=test.test6)
    dp.register_message_handler(test3_continuous, state=test.test7)
    dp.register_message_handler(test4_continuous, state=test.test8)
    dp.register_message_handler(test5_continuous, state=test.test9)
    dp.register_message_handler(test6_continuous, state=test.test10)
    #----------
    dp.register_message_handler(test2_perfect, state=test.test11)
    dp.register_message_handler(test3_perfect, state=test.test12)
    dp.register_message_handler(test4_perfect, state=test.test13)
    dp.register_message_handler(test5_perfect, state=test.test14)
    dp.register_message_handler(test6_perfect, state=test.test15)
    #-------
    dp.register_message_handler(test2_past, state=test.test16)
    dp.register_message_handler(test3_past, state=test.test17)
    dp.register_message_handler(test4_past, state=test.test18)
    dp.register_message_handler(test5_past, state=test.test19)
    dp.register_message_handler(test6_past, state=test.test20)
# -----------------------------------------------------------------------------------------------------------------------
