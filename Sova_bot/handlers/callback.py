from aiogram import types, Dispatcher
from aiogram.utils import executor
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import bot, dp 


@dp.callback_query_handler(lambda call: call.data == "button_call_1")
async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("NEXT", callback_data="button_call_2")
    markup.add(button_call_1)
    
    question = "Кто создатель Pythona?"
    answers = [
        "Harry Potter",
        "Putin",
        "Guida Van Rossum",
        "Voldemort",
        "Griffin",
        "Linus Tervaldo",
    ]
    
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type="quiz",
        correct_option_id=2,
        explanation="Лох",
        reply_markup=markup

    )

@dp.callback_query_handler(lambda call: call.data == "button_call_2")
async def quiz_3(call: types.CallbackQuery):
    
    question = "Кто это?"
    answers = [
        "Айдар",
        "Тимур",
        "Айбек",
        "Чынгыз",
        "Нурик",
        
    ]
    
    photo = open("media/photo_2022-12-19_03-17-49.jpg", "rb")
    await bot.send_photo(call.from_user.id, photo=photo)

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type="quiz",
        correct_option_id=2,
        explanation="Лох",
        
    )

def regisetr_handler_callback(dp:Dispatcher):
    dp.register_callback_query_handler(quiz_2, lambda call: call.data == "button_call_1")
    dp.register_callback_query_handler(quiz_3, lambda call: call.data == "button_call_2")
