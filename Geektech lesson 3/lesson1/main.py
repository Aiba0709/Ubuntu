





from aiogram import Bot, Dispatcher, executor, types
import config
import time
import random


bot = Bot(config.token)
dp = Dispatcher(bot) 

@dp.message_handler(commands=["start", "go"])
async def start(message : types.Message):
    with open("users.txt", "r",encoding="utf-8") as read_user:
        print(read_user.readlines())
    # with open("users.txt", "a+", encoding= 'utf-8') as users:
    #     users.write(f'{message.from_user.username}-{message.from_user.id}-{time.ctime()}\n')
    await message.answer (f"Здраствуйте, {message.from_user.full_name} {message.from_user.id}")

@dp.message_handler(commands=["help"])
async def start(message: types.Message):
    await message.reply("помощь")

@dp.message_handler(text = "Привет")
async def hello(message: types.Message):
    await message.answer("Привет")

@dp.message_handler()
async def not_found(message: types.Message):
    await message.reply("Я вас не понял введите /help")

executor.start_polling(dp)    


   


    