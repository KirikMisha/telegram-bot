# from telebot import types
# from telebot import TeleBot
# from config import BOT_TOKEN
# bot = TeleBot(BOT_TOKEN)
#
# def Grammar(message):
#     markup = types.ReplyKeyboardMarkup()
#     item1 = types.KeyboardButton('🕰️ Time')
#     item2 = types.KeyboardButton('👮‍♂ Rules')
#     item3 = types.KeyboardButton('⬅ Back')
#     markup.add(item1, item2, item3)
#     bot.send_message(message.chat.id, 'описание граматики', reply_markup=markup)
#
# def Time(message):
#     markup = types.ReplyKeyboardMarkup()
#     item1 = types.KeyboardButton('⏳Present simple', )
#     item2 = types.KeyboardButton('⌚Present continuous')
#     item3 = types.KeyboardButton('⏰Present perfect')
#     item4 = types.KeyboardButton('🔞Past simple')
#     item5 = types.KeyboardButton('⬅ Back')
#     markup.add(item1, item2, item3, item4, item5)
#     bot.send_message(message.chat.id, 'описание граматики', reply_markup=markup)
# def Present_simple(message):
#     markup = types.ReplyKeyboardMarkup()
#     item1 = types.KeyboardButton('🙈TestFirst')
#     item2 = types.KeyboardButton('⬅ Back')
#     markup.add(item1, item2)
#     bot.send_photo(message.chat.id, "http://lingvana.ru/wp-content/uploads/2014/03/Tablitsa-past-simpl-skan.png", reply_markup=markup)
# def Present_continuous(message):
#     markup = types.ReplyKeyboardMarkup()
#     item1 = types.KeyboardButton('🙈TestSecond')
#     item2 = types.KeyboardButton('⬅ Back')
#     markup.add(item1, item2)
#     bot.send_photo(message.chat.id, "https://preply.com/wp-content/uploads/2018/04/Tablitsa-prezent-kontinius-2.jpg", reply_markup=markup)
# def Present_perfect(message):
#     markup = types.ReplyKeyboardMarkup()
#     item1 = types.KeyboardButton('🙈TestЕhird')
#     item2 = types.KeyboardButton('⬅ Back')
#     markup.add(item1, item2)
#     bot.send_photo(message.chat.id, "https://lingvana.ru/wp-content/uploads/2014/02/Prezent-perfekt-tablitsa.png", reply_markup=markup)
# def Past_simple(message):
#     markup = types.ReplyKeyboardMarkup()
#     item1 = types.KeyboardButton('🙈TestFourth')
#     item2 = types.KeyboardButton('⬅ Back')
#     markup.add(item1, item2)
#     bot.send_photo(message.chat.id, "http://grammar-tei.com/wp-content/uploads/2016/10/shema.jpg", reply_markup=markup)
# def TestFourth(message):
#     markup = types.ReplyKeyboardMarkup()
#     item1 = types.KeyboardButton('invited')  # Правильный ответ
#     item2 = types.KeyboardButton('invite')
#     item3 = types.KeyboardButton('inviting')
#     item4 = types.KeyboardButton('⬅ Back')
#     markup.add(item1, item2, item3, item4)
#     bot.send_message(message.chat.id, 'I (to invite) __ your friend to the party.', reply_markup=markup)
# def Test2(message):
#     markup = types.ReplyKeyboardMarkup()
#     item1 = types.KeyboardButton('found')  # True answer
#     item2 = types.KeyboardButton('finds')
#     item3 = types.KeyboardButton('finded')
#     item4 = types.KeyboardButton('⬅ Back')
#     markup.add(item1, item2, item3, item4)
#     bot.send_message(message.chat.id, 'Paul (to find) __ a good and inexpensive hotel.', reply_markup=markup)
# def Test3(message):
#     markup = types.ReplyKeyboardMarkup()
#     item1 = types.KeyboardButton('understanded')
#     item2 = types.KeyboardButton('understand')
#     item3 = types.KeyboardButton('understood')   # Правильный ответ
#     item4 = types.KeyboardButton('⬅ Back')
#     markup.add(item1, item2, item3, item4)
#     bot.send_message(message.chat.id, 'We (to understand) __ each other..', reply_markup=markup)
# def Test4(message):
#     markup = types.ReplyKeyboardMarkup()
#     item1 = types.KeyboardButton('... didn’t play chess yesterday.') # Правильный ответ
#     item2 = types.KeyboardButton('... did no play chess yesterday.')
#     item3 = types.KeyboardButton('... not played chess yesterday.')
#     item4 = types.KeyboardButton('⬅ Back')
#     markup.add(item1, item2, item3, item4)
#     bot.send_message(message.chat.id, 'В каком варианте представлена отрицательная форма данного предложения: «Billy and Jim played chess yesterday»?', reply_markup=markup)
# def Test5(message):
#     markup = types.ReplyKeyboardMarkup()
#     item1 = types.KeyboardButton('had')
#     item2 = types.KeyboardButton('did sang')  # Правильный ответ
#     item3 = types.KeyboardButton('didn’t say')
#     item4 = types.KeyboardButton('⬅ Back')
#     markup.add(item1, item2, item3, item4)
#     bot.send_message(message.chat.id, ' В каком варианте ответа допущена ошибка?', reply_markup=markup)
# def Test6(message):
#     markup = types.ReplyKeyboardMarkup()
#     item1 = types.KeyboardButton('had.')   # Правильный ответ
#     item2 = types.KeyboardButton('did have')
#     item3 = types.KeyboardButton('did')
#     item4 = types.KeyboardButton('⬅ Back')
#     markup.add(item1, item2, item3, item4)
#     bot.send_message(message.chat.id, ' Дополните предложение “Andy … an interesting idea”, используя подходящую форму глагола:', reply_markup=markup)
# def Test7(massage):
#     markup = types.ReplyKeyboardMarkup()
#     item1 = types.KeyboardButton('She not looked alive.')  # Правильный ответ
#     item2 = types.KeyboardButton('The man introduced me to his wife last week.')
#     item3 = types.KeyboardButton('Yesterday I was getting very worried.')
#     item4 = types.KeyboardButton('⬅ Back')
#     markup.add(item1, item2, item3, item4)
#     bot.send_message(message.chat.id, ' Найдите предложение, в котором допущена ошибка:', reply_markup=markup)
# def Test8(message):
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
# def Test9(message):
#     markup = types.ReplyKeyboardMarkup()
#     item1 = types.KeyboardButton('did go')
#     item2 = types.KeyboardButton('go')  # Правильный ответ
#     item3 = types.KeyboardButton('gone')
#     item4 = types.KeyboardButton('⬅ Back')
#     markup.add(item1, item2, item3, item4)
#     bot.send_message(message.chat.id, 'Дополните предложение “Where did everybody … yesterday?”, используя подходящую форму глагола:', reply_markup=markup)
