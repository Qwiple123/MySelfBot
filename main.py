import asyncio
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram import Bot, Dispatcher, types, executor
import keyboards


storage = MemoryStorage()
bot = Bot(token = TOKEN)
dp = Dispatcher(bot=bot, storage=storage)

#class Dialog(StatesGroup:
@dp.message_handler(commands='start')
async def start(msg: types.Message):
    print(f'{msg.from_user.full_name} : start')
    await msg.answer("Здравствуйте меня зовут Максим 👋\nЯ начинающий Python разработчик 💡\nЧто бы узнать более подробную информацию обо мне нажмите на одну из кнопок ниже 👇👇👇", reply_markup=keyboards.main_keyboard()) 


@dp.callback_query_handler(text="gallery")
async def one_of_all(query: types.CallbackQuery):
    print(f'{query.from_user.full_name} : gallery')
    user_id = query.message.chat.id
    await query.message.delete()
    media = types.MediaGroup()
    media.attach_photo(types.InputFile('gallery/pic1.JPG'))
    media.attach_photo(types.InputFile('gallery/pic2.JPG'))
    await bot.send_media_group(user_id, media=media)
    await bot.send_message(user_id, 'Мои фотографии📷', reply_markup=keyboards.back_keyboard())






@dp.callback_query_handler(text="techno")
async def one_of_all(query: types.CallbackQuery):
    print(f'{query.from_user.full_name} : techno')
    user_id = query.message.chat.id
    await query.message.delete()
    await bot.send_message(user_id, """Технологии которые я уже изучил 📚\n
1. aiogram - Библиотека для написания ботов в телеграм✈️
2. bs4 и selenium - Библиотеки которые нужны для того что бы собирать информацию с сайтов
3. SQLite - Библиотека позволяющая создавать и использовать базы данных
4. Базовое знание алгоритмов
5. GIT \n\n
Технологии которые собираюсь учить 📖\n
1. SQL - обычный язык SQL поможет мне создавать более оптимизированные базы данных 💾
2. Docker - поможет разворачивать свои приложения на серверах с удобством и практичностью
3. Alembic - инструмент для миграций в базах данных
4. Django -Фреймворк для Backend-a с помощью которого можно делать сайты и веб приложения 🖥""", reply_markup=keyboards.back_keyboard())


@dp.callback_query_handler(text="impact")
async def one_of_all(query: types.CallbackQuery):
    print(f'{query.from_user.full_name} : impact')
    user_id = query.message.chat.id
    await query.message.delete()
    await bot.send_message(user_id, """Чем я могу быть полезен💡\n
1. Работать в команде и писать дополнительный функционал для вашего приложения🤝\n
2. Написать бота в телеграмм для сотрудников или клиентов вашей компании🤖\n
3. Создать базу данных и подключить ее к вашему приложению или телеграмм боту💾\n
Пользуясь моими услугами вы сможете получать больше обратной связи от клиентов или от сотрудников👥\n
Это пойдет вам на пользу в любом случае👍\n
Клиент будет больше пользоваться вашими услугами📱\n
А сотруднику будет удобнее их выполнять👨‍💻\n
Это как уменьшит расходы так и увеличит ваши доходы💵""", reply_markup=keyboards.back_keyboard())

@dp.callback_query_handler(text="contact")
async def one_of_all(query: types.CallbackQuery):
    print(f'{query.from_user.full_name} : contact')
    user_id = query.message.chat.id
    await query.message.delete()
    await bot.send_message(user_id, "Telegram: https://t.me/Qwiple51 📱\n\n VK: https://vk.com/qwiple_lare 💻\n\n GITHUB: https://github.com/Qwiple123 🖥", reply_markup=keyboards.back_keyboard())

@dp.callback_query_handler(text="projects")
async def one_of_all(query: types.CallbackQuery):
    print(f'{query.from_user.full_name} : projects')
    user_id = query.message.chat.id
    await query.message.delete()
    await bot.send_message(user_id, "У меня есть только один pet-проект это голосовой ассистент Карен\nВот репозиторий с исходным кодом на GITHUB🖥\nhttps://github.com/Qwiple123/Karen-Voice-Assistant", reply_markup=keyboards.back_keyboard())


@dp.callback_query_handler(text="back")
async def one_of_all(query: types.CallbackQuery):
    print(f'{query.from_user.full_name} : main_menu')
    user_id = query.message.chat.id
    await query.message.delete()
    await bot.send_message(user_id, "-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-Главное меню-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-", reply_markup=keyboards.main_keyboard())


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
