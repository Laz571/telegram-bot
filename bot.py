from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command
import asyncio

# Токен бота
TOKEN = "8156663778:AAGdFsreDfSSsimTEoPXgD-xm5UG84zeQZI"

# Создаем бота и диспетчер
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Обработчик команды /start
async def start_handler(message: Message):
    await message.answer("Привет! Я бот по недвижимости в Гулистане. Напиши /search, чтобы найти квартиру!")

# Обработчик команды /search
async def search_handler(message: Message):
    await message.answer("Скоро тут будет список квартир!")

# Регистрируем обработчики
dp.message.register(start_handler, Command("start"))
dp.message.register(search_handler, Command("search"))

# Функция запуска бота
async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

# Запускаем бота
asyncio.run(main())