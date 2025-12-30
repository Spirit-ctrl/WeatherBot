from aiogram.types import ReplyKeyboardMarkup, KeyboardButton




keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Погода 🌍"), KeyboardButton(text="Кол-во Осадков 🌧️")],
        [KeyboardButton(text="Сменить город ◀️"), KeyboardButton(text="Help 🚑")]
    ],
    resize_keyboard=True)