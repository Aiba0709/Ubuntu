# FSM - это Finite State Mashine (машина конечный состоянии)

from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from config  import bot
from keyboards.klient_kb import submit_markup, cancal_markup, gender_markup
from datebase.bot_db import sql_command_insert

class FSMAdmin(StatesGroup):
    name = State()
    age = State()
    gender  = State()
    region = State()
    photo = State()
    submit = State()


async def fsm_start(message: types.Message):
    if message.chat.type == "private":
        await FSMAdmin.name.set()
        await message.answer ("Салаам алейкум, как звать?", reply_markup=cancal_markup)
    else:
        await message.answer("пищи в личку")

async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        print(data)
        data ["id"] = message.from_user.id
        data ["username"] = f"@{message.from_user.username}"
        data["name"] = message.text
        print(data)
    await FSMAdmin.next()
    await message.answer("Скока лет?")    
     

async def load_age(message: types.Message, state: FSMContext):
    try:
        if 10 < int(message.text) < 50:
         async with state.proxy() as data:
          data ["age"] = int(message.text)       
         await FSMAdmin.next()
         await message.answer("Какой пол?", reply_markup=gender_markup)
        else:
            await message.answer("Доступ воспрещен")
    except:
        await message.answer("Пищи нормально")    


async def load_gender(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["gender"] = message.text        
    await FSMAdmin.next()
    await message.answer("Откуда будещь?", reply_markup=cancal_markup)

async def load_region(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["reegion"] = message.text        
    await FSMAdmin.next()
    await message.answer("Скинь фотку?")

async def load_photo(message: types.Message, state: FSMContext):
    print(message)
    async with state.proxy() as data:
        data["photo"] = message.photo[0].file_id
        await bot.send_photo(message.chat.id, data["photo"])            
    await FSMAdmin.next()
    await message.answer("Ты все верно написал данные?", reply_markup=submit_markup)

async def submit(message: types.Message, state: FSMContext):
    if message.text.lower() == "да":
        await sql_command_insert(state)
        await state.finish()
        await message.answer("Тогда свободен!")
    elif message.text.lower() == "Нет":
        await state.finish()
        await message.answer("Отмена")
    else:
        await message.answer("Нипонял?")        

async def cancel_reg(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is not None:
        await state.finish()
        await message.answer("Отмена")

def register_handlers_fsm_anketa(dp:Dispatcher):
    dp.register_message_handler(cancel_reg, state="*", commands=["cancel"])
    dp.register_message_handler(cancel_reg, Text(equals="отмена", ignore_case=True), state="*")
    dp.register_message_handler(fsm_start, commands=["reg"])               
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_age, state=FSMAdmin.age)
    dp.register_message_handler(load_gender, state=FSMAdmin.gender)
    dp.register_message_handler(load_region, state=FSMAdmin.region) 
    dp.register_message_handler(load_photo, state=FSMAdmin.photo, content_types=["photo"])
    dp.register_message_handler(submit, state=FSMAdmin.submit)