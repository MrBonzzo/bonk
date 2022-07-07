from asyncore import dispatcher
import logging
import os

from aiogram.utils.executor import start_webhook

from botapp.handlers import dp
from botapp.settings import WEBHOOK_PATH, WEBAPP_HOST, WEBAPP_PORT
from botapp.bot_actions import on_startup, on_shutdown


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    start_webhook(
        dispatcher=dp,
        webhook_path=WEBHOOK_PATH,
        skip_updates=True,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        host=WEBAPP_HOST,
        port=WEBAPP_PORT,
    )