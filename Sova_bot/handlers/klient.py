from aiogram import types, Dispatcher
from aiogram.utils import executor
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config import bot, dp 
from keyboards.klient_kb import start_markup


# @dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await bot.send_message(message.from_user.id, f"Hello {message.from_user.first_name}", reply_markup=start_markup)

async def info(message: types.Message):
    await bot.send_message(message.from_user.id, f"Сам разбирайся")

# @dp.message_handler(commands=["quiz"])
async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("NEXT", callback_data="button_call_1")
    markup.add(button_call_1)
    
    
    
    question = "Какая у меня любимая книга?"
    answers = [
        "1984",
        "Азбука"
        "Harry Potter",
        "Самурай без меча",
        "Джек Лондон"
    ]
    
    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type="quiz",
        correct_option_id=0,
        explanation="Лох",
        open_period=10,
        reply_markup=markup

    )

def register_handlers_klient(dp: Dispatcher):
    dp.register_message_handler(start, commands=["start"] )  
    dp.register_message_handler(quiz_1, commands=["quiz"] )  
    dp.register_message_handler(info, commands=["info"] )