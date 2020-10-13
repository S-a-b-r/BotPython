#/items
from aiogram.dispatcher.filters import Command
from aiogram.types import Message
from keyboards.inline.choice_buttons import choice

from loader import dp

@dp.message_handler(Command("items"))
async def show_items(message:Message):
    await message.answer(text = "На продажу есть 5 яблок и 1 груша. \n Eсли вам ничего не нужно - нажмите 'Отмена'", reply_markup = choice)
