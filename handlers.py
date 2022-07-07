from aiogram import types
from aiogram.dispatcher import Dispatcher

from settings import bot

dp = Dispatcher(bot)

@dp.message_handler()
async def echo(message: types.Message):
    if 'лучше всех' in message.text.lower():
        await message.answer('Лерка лучше всех!')
    else:
        await message.answer(f"""Все говорят '''{message.text}''', а ты купи слона""")
