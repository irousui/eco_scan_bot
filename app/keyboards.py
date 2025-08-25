from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder 

CALLBACK_BUTTON_ABOUT = "О нас ♻️"
CALLBACK_BUTTON_HELP ="Помощь ℹ️"
CALLBACK_BUTTON_SEND = "Отправить фото 🖼"

CALLBACK_BUTTON_PLASTIC = "Пластик🥤"
CALLBACK_BUTTON_PAPER = "Бумага 📚"
CALLBACK_BUTTON_GLASS = "Стекло 🫙"
CALLBACK_BUTTON_ALL = "Общий 🪒"
CALLBACK_BUTTON_BACK = "⬅️⬅️⬅️"

CALLBACK_BUTTON_ALL_WHAT = "Что такое общий мусор 🤔"


main_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text=CALLBACK_BUTTON_ABOUT)],
    [KeyboardButton(text=CALLBACK_BUTTON_HELP)],
    [KeyboardButton(text=CALLBACK_BUTTON_SEND)]
],
                    resize_keyboard=True,
                    input_field_placeholder='Выберите действие:'
)


recycling_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text=CALLBACK_BUTTON_PLASTIC), KeyboardButton(text=CALLBACK_BUTTON_PAPER)],
    [KeyboardButton(text=CALLBACK_BUTTON_GLASS), KeyboardButton(text=CALLBACK_BUTTON_ALL)],
    [KeyboardButton(text='Назад')]
],
                    resize_keyboard=True,
                    input_field_placeholder='Выберите категорию ♻️'                    
)

recycling_all = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text=CALLBACK_BUTTON_BACK)]
],
                    resize_keyboard=True
                    # input_field_placeholder=''  
)

recycling_trash_all = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text=CALLBACK_BUTTON_ALL_WHAT)],
    [KeyboardButton(text=CALLBACK_BUTTON_BACK)]
],
                    resize_keyboard=True,
                    # input_field_placeholder='...'  
)