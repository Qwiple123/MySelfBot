import asyncio
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram import Bot, Dispatcher, types, executor
TOKEN = '5913399795:AAEUP-slfC2rMUugkOoU0MEW_CnqnIrCezA'

storage = MemoryStorage()
bot = Bot(token = TOKEN)
dp = Dispatcher(bot=bot, storage=storage)

#class Dialog(StatesGroup:
@dp.message_handler(commands='start')
async def start(msg: types.Message):
    await msg.answer("Приветствую в боте Avtosearch!") 


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)