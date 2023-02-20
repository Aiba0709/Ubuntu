from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from pytube import YouTube
import conf
import logging
import os

bot = Bot(token=config.token)
dp = Dispatcher(bot, storage=MemoryStorage())
storage = MemoryStorage()
logging.basicConfig(level=logging.INFO)

audio_button = KeyboardButton("Аудио")
video_button = KeyboardButton("Видео")

butttons = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
butttons.add(audio_button)
butttons.add(video_button)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer(f"""Здраствуйте, {message.from_user.full_name}
Я вам помогу скачать аудио или же видео с ютуба""", reply_markup=butttons)

class DownloadAudio(StatesGroup):
    download = State()

class DownloadVideo(StatesGroup):
    download = State()

def download(url, type):
    yt = YouTube(url)
    if type == "audio":
        yt.streams.filter(only_audio=True).first().download("audio", f"{yt.title}.mp3")
        return f"{yt.title}.mp3"
    elif type == "video":
        yt.streams.filter(progressive=True, file_extension="mp4").first().download("video", f"{yt.title}.mp4")
        return f"{yt.title}.mp4"

@dp.message_handler(text = ["Аудио", "аудио", "Audio", "audio"])
async def audio(message: types.Message):
    await message.answer("Отправьте ссылку на видео и я вам отправлю его в mp3")
    await DownloadAudio.download.set()

@dp.message_handler(text = ["Видео", "видео", "Video", "video"])
async def video(message: types.Message):
    await message.answer("Отправьте ссылку на видео в ютубе и я вам его отправлю")
    await DownloadVideo.download.set()

@dp.message_handler(state=DownloadAudio.download)
async def download_audio(message: types.Message, state : FSMContext):
    try:
        title = download(message.text, "audio")
        audio = open(f"audio/{title}", "rb")
        await message.answer("Скачиваем файл ожидайте...")
        try:
            await message.answer("Все скачалось вот держи")
            await bot.send_audio(message.chat.id, audio)
        except:
            await message.answer("Произошла ошибка, попробуйте позже")
        os.remove(f'audio/{title}')
        await state.finish()
    except:
        await message.answer("Неверная ссылка на видео")
        await state.finish()

@dp.message_handler(state=DownloadVideo.download)
async def download_video(message: types.Message, state : FSMContext):
    await message.answer("Скачиваем видео файл ожидайте...")
    try:
        title = download(message.text, "video")
        video = open(f"video/{title}", "rb")
        try:
            await message.answer("Все скачалось вот держи")
            await bot.send_video(message.chat.id, video)
        except:
            await message.answer("Произошла ошибка, попробуйте позже")
        os.remove(f'video/{title}')
        await state.finish()
    except:
        await message.answer("Неверная ссылка на видео")
        await state.finish()

@dp.message_handler()
async def not_found(message: types.Message):
    await message.reply("Я вас не понял", reply_markup=butttons)

executor.start_polling(dp, timeout=1000000)