from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton
)

main = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Место регистрации"),
            KeyboardButton(text="Место праздника")
        ],
        [
            KeyboardButton(text="Программа праздника"),
            KeyboardButton(text="Подтвердить своё присутствие", request_contact=True)
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=False,
    input_field_placeholder="Выберите действие из меню",
    selective=True
)