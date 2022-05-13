from config import bot, Dispatcher
from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton,CallbackQuery


# Развёртка меню ссылок-------------------------------------------------------------------------------------------------
async def links_menu(callback: CallbackQuery):
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    item1 = InlineKeyboardButton('Запоминание слов',
                                 url='https://lengvipark.ru/blog/55-kak-bystro-zapominat-anglijskie-slova')
    item2 = InlineKeyboardButton('Блог «Инглекс»', url='https://englex.ru/articles/')
    item3 = InlineKeyboardButton('Наши контакты', callback_data='contact_details')
    item4 = InlineKeyboardButton('⬅ Back to menu', callback_data='back_menu')
    markup = InlineKeyboardMarkup(row_width=1)
    markup.add(item1, item2, item3, item4)
    await callback.message.answer('В этом разделе находится подборка сайтов, которые наверняка помогут тебе в изучении '
                                  'английского\n'
                                  'Первая ссылка перекинет тебя на сайт, где можно более подробно изучить вопрос '
                                  'быстрого и качественного запоминания английских слов\n'
                                  'Вторая ссылка приведет вас на сайт "Инглекс блог" где постятся очень полезные и '
                                  'интересные статьи об английском языке\n'
                                  'Третья же кнопочка выведет вам контактные данные разработчиков этого бота, если у '
                                  'вас появились какие нибуть вопросы или же предложения, не стесняйтесь, пишите',
                                  reply_markup=markup)
#-----------------------------------------------------------------------------------------------------------------------


# Контактные данные-----------------------------------------------------------------------------------------------------
async def contact_details(callback: CallbackQuery):
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    item1 = InlineKeyboardButton('VK',
                                 url='https://vk.com/improbusbastardis')
    item2 = InlineKeyboardButton('Gmail', url='https://mail.google.com/')
    item3 = InlineKeyboardButton('⬅ Back to menu', callback_data='back_menu')
    markup = InlineKeyboardMarkup(row_width=1)
    markup.add(item1, item2, item3)
    await callback.message.answer('Gmail: omniabene969@gmail.com\n'
                                  'Есле же вы хотите поддержать проект, то можете выполнить перевод *номер карты*'
                                  '',reply_markup=markup)

#-----------------------------------------------------------------------------------------------------------------------


def expanded_links_f(dp: Dispatcher):
    dp.register_callback_query_handler(links_menu, text='links_menu')
    dp.register_callback_query_handler(contact_details, text='contact_details')