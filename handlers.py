from aiogram import types
from aiogram.dispatcher import Dispatcher

from settings import bot

dp = Dispatcher(bot)

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)
