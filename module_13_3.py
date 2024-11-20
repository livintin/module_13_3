from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

api = '7729780471:AAH4b9OOKAOwV6EPMBxfe6iv6RUHC7J53m0'
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=['start'])
async def urban_message(message):
    print("Start")
    await message.answer('Привет! Я бот помогающий твоему здоровью.')


@dp.message_handler()
async def all_message(message):
    print("Мы получили сообщение!")
    await message.answer('Введите команду /start, чтобы начать общение.')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
