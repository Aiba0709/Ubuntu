

from aiogram import Bot, Dispatcher, executor, types
import config 
import time
import sqlite3

connect = sqlite3.connect("users.db")
cur = connect.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS users(
    usersname VARCHAR(255),
    id INTEGER,
    created DATE
    );
    """)
connect.commit()    


bot = Bot(config.token)
dp = Dispatcher(bot) 

@dp.message_handler(commands=["start", "go"])
async def start(message : types.Message):
    cur = connect.cursor()
    cur.execute(f"CELECT id FROM users WHERE id == {message.from_user.id};")
    result = cur.fetchall()
    await message.answer (f"Здраствуйте, {message.from_user.full_name} {message.from_user.id}")

@dp.message_handler(commands=["help"])
async def start(message: types.Message):
    await message.reply("помощь")

@dp.message_handler(text = "Привет")
async def hello(message: types.Message):
    await message.answer("Привет")

@dp.message_handler(commands=["users"])
async def get_users(message: types.Message):
    cur = connect.cursor()
    cur.execute("CELECT * FROM users;")
    res = cur.fetchall()
    if res != []:
       await message.answer(res)
    else:
        await message.answer("Список пуст")   

@dp.message_handler()
async def not_found(message: types.Message):
    await message.reply("Я вас не понял введите /help")

executor.start_polling(dp)