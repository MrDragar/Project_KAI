from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from src.callbacks import FeedbackCallback

main = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text="Об Университете")],
        [KeyboardButton(text="📞 Контакты 📞")],
        [KeyboardButton(text="🎓 Направления обучения 🎓")],
        [KeyboardButton(text="🕺 Студенческая жизнь 🕺")],
        [KeyboardButton(text="🕺 Обратная связь 🕺")]
    ],
    resize_keyboard=True
)

napravl_oboch = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text="Институт авиации, наземного транспорта и энергетики (ИАНТЭ)")],
        [KeyboardButton(text="Физико-математический факультет (ФМФ)")],
        [KeyboardButton(text="Институт автоматики и электронного приборостроения (ИАЭП)")],
        [KeyboardButton(text="Институт компьютерных технологий и защиты информации (ИКТЗИ)")],
        [KeyboardButton(text="Институт радиоэлектроники, фотоники и цифровых технологий (ИРЭФ-ЦТ)")],
        [KeyboardButton(text="Институт инженерной экономики и предпринимательства (ИИЭиП)")],
        [KeyboardButton(text="🔼 Вернуться в меню 🔼")]
    ],
    resize_keyboard=True
)

contact_kb = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text="💬 Написать сообщение 💬")],
        [KeyboardButton(text="🔼 Вернуться в меню 🔼")]
    ],
    resize_keyboard=True
)


stud_life = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text="🖼 Смотреть фото 🖼")],
        [KeyboardButton(text="🔼 Вернуться в меню 🔼")]
    ],  
    resize_keyboard=True
)


def get_feedback_keyboard(user_id: int) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardBuilder()
    keyboard.button(
        text="Ответить пользователю",
        callback_data=FeedbackCallback(user_id=user_id).pack()
    )
    return keyboard.as_markup()
