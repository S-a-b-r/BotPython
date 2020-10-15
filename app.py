from loader import bot, storage
from aiogram import executor
from handlers import dp
from config import admin_id


async def on_shutdown(dp):
    await bot.close()
    await storage.close()
    await bot.send_message(chat_id = admin_id, text = "Бот выключен")


async def send_to_admin(dp):
    await bot.send_message(chat_id = admin_id, text = "Бот запущен")

if __name__ == '__main__':
    executor.start_polling(dp, on_shutdown=on_shutdown, on_startup=send_to_admin)
