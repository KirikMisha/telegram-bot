
from telebot import TeleBot
from config import BOT_TOKEN
import sqlite3
bot = TeleBot(BOT_TOKEN)


global sql
global db
db = sqlite3.connect('TGBot.db',check_same_thread=False)
sql = db.cursor()



def Base(message):
    sql.execute("""CREATE TABLE IF NOT EXISTS users(
        id INTEGER,
        number_ordinary_words INTEGER,
        number_Irregular_verbs INTEGER
    )""")
    db.commit()
    user_id = int(message.chat.id)
    sql.execute(f"SELECT id FROM users WHERE id = '{user_id}'")
    if sql.fetchone() is None:
        sql.execute(f"INSERT INTO users VALUES(?, ?, ?)", (user_id, 0, 0))
        db.commit()

def Plass(message, a):
    user_id = int(message.chat.id)
    for i in sql.execute(f"SELECT number_ordinary_words FROM users WHERE id = '{user_id}'"):
        balance = i[0]
    sql.execute(f"UPDATE users SET number_ordinary_words = {balance+a} WHERE id = '{user_id}'")
    db.commit()
    return balance

def PlassI(message, a):
    user_id = int(message.chat.id)
    for i in sql.execute(f"SELECT number_Irregular_verbs FROM users WHERE id = '{user_id}'"):
        balance = i[0]
    sql.execute(f"UPDATE users SET number_Irregular_verbs = {balance+a} WHERE id = '{user_id}'")
    db.commit()
    return balance

def Restart_ordinary_words(message):
    user_id = int(message.chat.id)
    sql.execute(f"UPDATE users SET number_ordinary_words = {0} WHERE id = '{user_id}'")
    db.commit()

def Restart_Irregular_verbs(message):
    user_id = int(message.chat.id)
    sql.execute(f"UPDATE users SET number_Irregular_verbs = {0} WHERE id = '{user_id}'")
    db.commit()