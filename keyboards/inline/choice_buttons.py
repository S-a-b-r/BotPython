from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.inline.callback_datas import buy_callback
choice = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text = "Купить груши", callback_data = "buy:pear:1"),
            InlineKeyboardButton(text = "Купить яблоки", callback_data = "buy:apples:1")
        ],
        [
            InlineKeyboardButton(text = "Отмена", callback_data="cansel")
        ]
    ]
)