import asyncio
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram import Bot, Dispatcher, types, executor
import keyboards
TOKEN = '5913399795:AAEUP-slfC2rMUugkOoU0MEW_CnqnIrCezA'

storage = MemoryStorage()
bot = Bot(token = TOKEN)
dp = Dispatcher(bot=bot, storage=storage)

#class Dialog(StatesGroup:
@dp.message_handler(commands='start')
async def start(msg: types.Message):
    await msg.answer("Приветствую!!", reply_markup=keyboards.main_menu_reply()) 

@dp.message_handler(lambda message: message.text == "Галерея")
async def gallery(msg: types.Message):
        media = types.MediaGroup()
        media.attach_photo(types.InputFile('gallery/pic1.JPG'), 'Превосходная фотография')
        media.attach_photo(types.InputFile('gallery/pic2.JPG'), 'Eще одна превосходная фотография')
        await msg.answer_media_group(media=media)

@dp.message_handler(lambda message: message.text == "Стек технологий")
async def techno(msg: types.Message):
        await msg.answer("""Технологии которые я уже изучил \n
1. aiogram (Библиотека для написания ботов в телеграм,\n    на ней я и написал этого бота)
2. bs4 и selenium (Библиотеки которые нужны для того что бы\n    собирать информацию с сайтов
3. SQLite (Библиотека позволяющая создавать и использовать\n    реляционные базы данных)
4. Базовое знание алгоритмов
5. GIT \n\nТехнологии которые собираюсь учить \n
1. SQL обычный язык SQL поможет мне создавать более \n    оптимизированные базы данных
2. Docker поможет разворачивать свои приложения на \n    серверах с удобством и практичностью
3. Alembic инструмент для миграций в базах данных
4. Django Фреймворк для Backend-a с помощью которого \n    можно делать сайты и веб приложения """)




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)