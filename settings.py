import os

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher

BOT_TOKEN = os.getenv('BOT_TOKEN')
HOSTNAME = os.getenv('HOSTNAME')

# webhook settings
WEBHOOK_HOST = f'https://{HOSTNAME}.herokuapp.com'
WEBHOOK_PATH = f'/webhook/{BOT_TOKEN}'
WEBHOOK_URL = f'{WEBHOOK_HOST}{WEBHOOK_PATH}'

# webserver settings
WEBAPP_HOST = os.getenv('WEBAPP_HOST')
WEBAPP_PORT = os.getenv('WEBAPP_PORT')

bot = Bot(BOT_TOKEN)