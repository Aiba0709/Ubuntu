from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

start_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True
)

start_button = KeyboardButton("start")
info_button = KeyboardButton("info")

share_locaation = KeyboardButton("share location", request_location=True)

start_markup.add(start_button, info_button).add(share_locaation)

submit_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
).add(
    KeyboardButton("Да"),
    KeyboardButton("Нет")
)

cancal_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True
).add(
    KeyboardButton("Отмена")
)

gender_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
    row_width=3
).add(
    KeyboardButton("Мужчина"),
    KeyboardButton("Женщина"),
    KeyboardButton("Незнаю"),
    KeyboardButton("Отмена")    
)


