from aiogram import types
from aiogram.dispatcher import Dispatcher

from settings import bot
from keyboards import start_keyboard

dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def start_message(message: types.Message):
    await message.answer(text="Привет! Смотри что я умею :)", reply_markup=start_keyboard)


@dp.message_handler()
async def terminate_text_message(message: types.Message):
    if message.text == "Загрузить картинку":
        await message.answer(text="Ну загружай, кто тебе мешает, ААА??!?!?")
    elif message.text == "Глянуть что уже есть в базе":
        await message.answer(text="Ничо нет")
    else:
        await message.answer(text="Нииичо не понимаю, ткни лучше в кнопки", reply_markup=start_keyboard)
