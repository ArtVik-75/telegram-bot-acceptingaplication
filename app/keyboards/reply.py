from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Оставить заявку")]
    ],
    resize_keyboard=True
)