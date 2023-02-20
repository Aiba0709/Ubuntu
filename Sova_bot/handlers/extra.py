from aiogram import types, Dispatcher
from config import bot, dp

# @dp.message_handler()
async def echo(message: types.Message):
    ploxie_slova = ["сука", "пидораз", "гондон", "блять"]
    for slova in ploxie_slova:
       if slova in message.text.lower():
        await bot.delete_message(message.chat.id, message.message_id)
        if message.from_user.username is not None:
            await bot.send_message(message.chat.id, f"Не матерись @{message.from_user.username} Сам ты {slova}")
        else:
            await bot.send_message(message.chat.id, f"Не матерись @{message.from_user.first_name} Сам ты {slova}")
    if message.text.startswith("."):
        await bot.pin_chat_message(message.chat.id, message.message_id)   


    # print(message) 
    # await bot.send_message(message.from_user.id, message.text)

def register_handlers_extra(dp:Dispatcher):
    dp.register_message_handler(echo)    