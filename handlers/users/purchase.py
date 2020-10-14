#/items
from aiogram.dispatcher.filters import Command
from aiogram.types import Message,CallbackQuery
from keyboards.inline.choice_buttons import choice, pear_keyboard, apple_keyboard
import logging


from loader import dp

@dp.message_handler(Command("items"))
async def show_items(message:Message):
    await message.answer(text = "На продажу есть яблоки и груши. \n Eсли вам ничего не нужно - нажмите 'Отмена'", reply_markup = choice)

@dp.callback_query_handler(text_contains="pears")
async def buing_pear(call: CallbackQuery):
    await call.answer(cache_time = 60)
    callback_data = call.data
    logging.info(f"call = {callback_data}")
    await call.message.answer("Вы выбрали грушу", reply_markup = pear_keyboard)

@dp.callback_query_handler(text_contains="apples")
async def buing_apple(call: CallbackQuery):
    await call.answer(cache_time = 60)
    callback_data = call.data
    logging.info(f"call = {callback_data}")
    await call.message.answer("Вы выбрали яблоки", reply_markup = apple_keyboard)

@dp.callback_query_handler(text_contains = "cansel")
async def cancel_buying(call: CallbackQuery):
    await call.answer("Вы отменили покупку!", show_alert = True)
    await call.message.edit_reply_markup()