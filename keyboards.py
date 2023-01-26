from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def main_menu_reply():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    
    keyboard.add(
        KeyboardButton(text='Галерея'),
        KeyboardButton(text="Стек технологий"),
        KeyboardButton(text="Чем могу быть полезен"),
        KeyboardButton(text="Контакты"),
        KeyboardButton(text="пока незнаю...")
        )
    return keyboard