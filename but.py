from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
main_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Слово командира", callback_data="word_commander")],
    [InlineKeyboardButton(text="Про полк FENIX", callback_data="about_phoenix")],
    [InlineKeyboardButton(text="Вакансії", callback_data="vacancies")],
    [InlineKeyboardButton(text="Відправити анкету", callback_data="anketa")],
    [InlineKeyboardButton(text="Новини FENIX", callback_data="channel")],
    [InlineKeyboardButton(text="Визнання", callback_data="viz")],
    [InlineKeyboardButton(text="Наші переваги", callback_data="perevag")]
])



back = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Назад", callback_data="back")],
])




inline = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Інженер БпЛА", callback_data="inzhenerbpla")],
        [InlineKeyboardButton(text="Технік БпЛА", callback_data="tekhnikbpla")],
        [InlineKeyboardButton(text="Водій екіпажу БпЛА", callback_data="vodiybpla")],
        [InlineKeyboardButton(text="Інженер-сапер БпЛА", callback_data="saperbpla")],
        [InlineKeyboardButton(text="Бойовий медик", callback_data="medyk")],
        [InlineKeyboardButton(text="Оператор РЕБ/РЕР", callback_data="rebrer")],
        [InlineKeyboardButton(text="Майстер-вибухотехник БпЛА", callback_data="vybuh")],
        [InlineKeyboardButton(text="Майстер з ремонту БпЛА", callback_data="remont")],
        [InlineKeyboardButton(text="Діловод", callback_data="dilovod")],
        [InlineKeyboardButton(text="Відеооператор-режисер монтажу", callback_data="video")],
        [InlineKeyboardButton(text="Черговий пункту управління", callback_data="chergovyy")],
        [InlineKeyboardButton(text="Інструктор БпЛА", callback_data="instruktor")],
        [InlineKeyboardButton(text="Зв'язківець (ІТ-напрямок)", callback_data="it")],
        [InlineKeyboardButton(text="Зв'язківець (Радіозв'язок)", callback_data="radio")],
        [InlineKeyboardButton(text="Військовий психолог", callback_data="psycholog")],
        [InlineKeyboardButton(text="Поліграфолог", callback_data="poligrafolog")],
        [InlineKeyboardButton(text="SMM-Менеджер", callback_data="smm")],
        [InlineKeyboardButton(text="Фінансист", callback_data="finansyst")],
        [InlineKeyboardButton(text="Фахівець з публічних закупівель", callback_data="zakupivli")],
        [InlineKeyboardButton(text="Графічний дизайнер", callback_data="dyzayner")],
        [InlineKeyboardButton(text="Назад", callback_data="back")]
    ]
)





reply_pos = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Інженер БпЛА")],
        [KeyboardButton(text="Технік БпЛА")],
        [KeyboardButton(text="Водій екіпажу БпЛА")],
        [KeyboardButton(text="Інженер-сапер БпЛА")],
        [KeyboardButton(text="Бойовий медик")],
        [KeyboardButton(text="Оператор РЕБ/РЕР")],
        [KeyboardButton(text="Майстер-вибухотехник БпЛА")],
        [KeyboardButton(text="Майстер з ремонту БпЛА")],
        [KeyboardButton(text="Діловод")],
        [KeyboardButton(text="Відеооператор-режисер монтажу")],
        [KeyboardButton(text="Черговий пункту управління")],
        [KeyboardButton(text="Інструктор БпЛА")],
        [KeyboardButton(text="Зв'язківець (ІТ-напрямок)")],
        [KeyboardButton(text="Зв'язківець (Радіозв'язок)")],
        [KeyboardButton(text="Військовий психолог")],
        [KeyboardButton(text="Поліграфолог")],
        [KeyboardButton(text="SMM-Менеджер")],
        [KeyboardButton(text="Фінансист")],
        [KeyboardButton(text="Фахівець з публічних закупівель")],
        [KeyboardButton(text="Графічний дизайнер")],
    ],
)