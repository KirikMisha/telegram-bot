
from telebot import TeleBot
from config import BOT_TOKEN
import sqlite3
bot = TeleBot(BOT_TOKEN)







def Base(message):
    db = sqlite3.connect('TGBot.db')
    sql = db.cursor()
    sql.execute("""CREATE TABLE IF NOT EXISTS users(
        id INTEGER,
        number_words INTEGER
    )""")
    db.commit()
    user_id = int(message.chat.id)
    sql.execute(f"SELECT id FROM users WHERE id = '{user_id}'")
    if sql.fetchone() is None:
        sql.execute(f"INSERT INTO users VALUES(?, ?)", (user_id, 0))
        db.commit()


