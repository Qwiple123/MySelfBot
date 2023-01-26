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
    await msg.answer("Привет меня зовут Максим \nЯ начинающий Python разработчик\nЯ делаю этого бота что бы попрактиковать свои навыки", reply_markup=keyboards.main_keyboard()) 


@dp.callback_query_handler(text="gallery")
async def one_of_all(query: types.CallbackQuery):
    user_id = query.message.chat.id
    await query.message.delete()
    media = types.MediaGroup()
    media.attach_photo(types.InputFile('gallery/pic1.JPG'), 'Превосходная фотография')
    media.attach_photo(types.InputFile('gallery/pic2.JPG'), 'Eще одна превосходная фотография')
    await bot.send_media_group(user_id, media=media)
    await bot.send_message(user_id, 'Мои фотографии', reply_markup=keyboards.back_keyboard())






@dp.callback_query_handler(text="techno")
async def one_of_all(query: types.CallbackQuery):
    user_id = query.message.chat.id
    await query.message.delete()
    await bot.send_message(user_id, """Технологии которые я уже изучил \n
1. aiogram (Библиотека для написания ботов в телеграм,\n    на ней я и написал этого бота)
2. bs4 и selenium (Библиотеки которые нужны для того что бы\n    собирать информацию с сайтов)
3. SQLite (Библиотека позволяющая создавать и использовать\n    реляционные базы данных)
4. Базовое знание алгоритмов
5. GIT \n\n
Технологии которые собираюсь учить \n
1. SQL обычный язык SQL поможет мне создавать более \n    оптимизированные базы данных
2. Docker поможет разворачивать свои приложения на \n    серверах с удобством и практичностью
3. Alembic инструмент для миграций в базах данных
4. Django Фреймворк для Backend-a с помощью которого \n    можно делать сайты и веб приложения """, reply_markup=keyboards.back_keyboard())


@dp.callback_query_handler(text="impact")
async def one_of_all(query: types.CallbackQuery):
    user_id = query.message.chat.id
    await query.message.delete()
    await bot.send_message(user_id, "Я могу написать бота в телеграм, парсер сайта\nСоздать базу данных или автоматизировать любой процесс", reply_markup=keyboards.back_keyboard())

@dp.callback_query_handler(text="contact")
async def one_of_all(query: types.CallbackQuery):
    user_id = query.message.chat.id
    await query.message.delete()
    await bot.send_message(user_id, "Telegram: https://t.me/Qwiple51\n VK: https://vk.com/qwiple_lare\n GITHUB: https://github.com/Qwiple123", reply_markup=keyboards.back_keyboard())

@dp.callback_query_handler(text="projects")
async def one_of_all(query: types.CallbackQuery):
    user_id = query.message.chat.id
    await query.message.delete()
    await bot.send_message(user_id, "Пока у меня есть только один маленький pet-проект это голосовой ассистент Карен\nВот репозиторий с исходным кодом на GITHUB\nhttps://github.com/Qwiple123/Karen-Voice-Assistant", reply_markup=keyboards.back_keyboard())


@dp.callback_query_handler(text="back")
async def one_of_all(query: types.CallbackQuery):
    user_id = query.message.chat.id
    await query.message.delete()
    await bot.send_message(user_id, "Главное меню", reply_markup=keyboards.main_keyboard())


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)