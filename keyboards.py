from ctypes import resize
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton

image_button = KeyboardButton("Загрузить картинку")
lookup_button = KeyboardButton("Глянуть что уже есть в базе")

start_keyboard = (
    ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    .row(image_button)
    .row(lookup_button)
)
