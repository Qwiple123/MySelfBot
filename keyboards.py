from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def main_menu_reply():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    
    keyboard.add(
        KeyboardButton(text='Галерея'),
        KeyboardButton(text="Стек технологий"),
        KeyboardButton(text="Чем могу быть полезен"),
        KeyboardButton(text="Контакты"),
        KeyboardButton(text="Мои проекты")
        )
    return keyboard

def main_keyboard():
    keyboard = types.InlineKeyboardMarkup(row_width=3)
    keyboard.add(types.InlineKeyboardButton(text="Галерея 🌅", callback_data="gallery"),
    types.InlineKeyboardButton(text="Стек технологий 🎛", callback_data="techno"))
    keyboard.add(types.InlineKeyboardButton(text="Чем могу быть полезен 💡", callback_data="impact"))
    keyboard.add(types.InlineKeyboardButton(text="Контакты ☎️", callback_data="contact"),
    types.InlineKeyboardButton(text="Мои проекты 🛠", callback_data="projects"))

    return keyboard

def back_keyboard():
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="back"))


    return keyboard