from aiogram import types
import sqlite3
from config import bot


global sql
global db
db = sqlite3.connect('TGBot.db',check_same_thread=False)
sql = db.cursor()


async def Base(message: types.Message):
    sql.execute("""CREATE TABLE IF NOT EXISTS users(
        id INTEGER,
        number_ordinary_words INTEGER,
        number_Irregular_verbs INTEGER,
        number_Basic_stable_expressions INTEGER
    )""")
    db.commit()
    user_id = int(message.chat.id)
    sql.execute(f"SELECT id FROM users WHERE id = '{user_id}'")
    if sql.fetchone() is None:
        sql.execute(f"INSERT INTO users VALUES(?, ?, ?, ?)", (user_id, 0, 0, 0))
        db.commit()


def plass(message, column, number_of_words):
    user_id = int(message.chat.id)
    for i in sql.execute(f"SELECT {column} FROM users WHERE id = '{user_id}'"):
        balance = i[0]
    sql.execute(f"UPDATE users SET {column} = {balance + number_of_words} WHERE id = '{user_id}'")
    db.commit()
    return balance


async def restart_words(message, column):
    user_id = int(message.chat.id)
    sql.execute(f"UPDATE users SET {column} = {0} WHERE id = '{user_id}'")
    db.commit()
    await bot.send_message(message.chat.id, f'Ваши результаты по {column} обнулены')
