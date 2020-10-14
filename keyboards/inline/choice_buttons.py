from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.inline.callback_datas import buy_callback
import config
choice = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text = "Купить груши", callback_data = "buy:pears:1"),
            InlineKeyboardButton(text = "Купить яблоки", callback_data = "buy:apples:1")
        ],
        [
            InlineKeyboardButton(text = "Отмена", callback_data="cansel")
        ]
    ]
)

pear_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text = "Купи груши тут", url = config.URL_PEAR)
        ]
    ]
)
apple_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text = "Купи яблоки тут", url = config.URL_APPLES)
        ]
    ]
)