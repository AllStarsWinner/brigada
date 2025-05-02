from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

main = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Слово комбрига")], [KeyboardButton(text='Відправити анкету')],
        [KeyboardButton(text="Про бригаду Фенікс")],
        [KeyboardButton(text="Інженер БпЛА")], [KeyboardButton(text="Технік БпЛА")],
        [KeyboardButton(text="Водій екіпажу БпЛА")], [KeyboardButton(text="Інженер-сапер БпЛА")],
        [KeyboardButton(text="Бойовий медик")], [KeyboardButton(text="Оператор РЕБ/РЕР")],
        [KeyboardButton(text="Майстер-вибухотехник Бпла")], [KeyboardButton(text="Майстер з ремонту БпЛА")],
        [KeyboardButton(text="Діловод")], [KeyboardButton(text="Відеооператор-режисер монтажу")],
        [KeyboardButton(text="Черговий пункту управління")], [KeyboardButton(text="Інструктор БпЛА")],
        [KeyboardButton(text="Зв'язківець (ІТ-напрямок)")], [KeyboardButton(text="Зв'язківець (Радіозв'язок)")],
        [KeyboardButton(text="Військовий психолог")], [KeyboardButton(text="Поліграфолог")],
        [KeyboardButton(text="SMM-менеджер")], [KeyboardButton(text="Фінансист")],
        [KeyboardButton(text="Фахівець з публічних закупівель")], [KeyboardButton(text="Графічний дизайнер")],
    ]
)