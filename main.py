import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, FSInputFile, ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.filters import CommandStart, Command
from aiogram.enums import ParseMode
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.context import FSMContext
import datetime
import re
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.enums import ParseMode
import but
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder
import but as kb
import text
from but import main_inline
import smtplib
from email.mime.text import MIMEText
from aiogram import Bot, Dispatcher, types
from aiogram.types import CallbackQuery, Message, ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

# 7131545198

# Ініціалізація бота
bot = Bot(token='7613826272:AAGSqSR8PTfG5w3yCaV3-6pQH1AjPdKfVy8')
dp = Dispatcher(storage=MemoryStorage())  # Обов’язково додати storage

# ID адміна
ADMIN_CHAT_ID = 892519055


###########textttextexetxetxetxtx

@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("""Твоя сила — наша перевага!
Вітаємо в боті полку FENIX. Заповни анкету, переглянь вакансії та зроби перший крок до служби в одному з найефективніших підрозділів ДПСУ.""",
                         reply_markup=but.main_inline)


@dp.callback_query(F.data == 'vacancies')
async def cmd_heart(callback: CallbackQuery):
    await callback.message.edit_text("Дізнайтеся більше про посаду мрії, натиснувши на кнопки снизу",
                                     reply_markup=but.inline)


@dp.callback_query(F.data == 'word_commander')
async def cmd_heart(callback: CallbackQuery):
    await callback.message.edit_text("""Хочешь бути корисним для своєї країни? 

Готовий її захищати?
Згоден опановувати нові навички?
ПРИЄДНУЙСЯ ДО НАС!!!

Україна чекає на тебе

Командир полку Дмитро Олексюк
Подати анкету можна на сайті https://fxdpsu.com або у боті""", reply_markup=but.back)


@dp.callback_query(F.data == 'viz')
async def cmd_heart(callback: CallbackQuery):
    await callback.message.edit_text(text.link, reply_markup=but.back)


@dp.callback_query(F.data == 'about_phoenix')
async def cmd_heart(callback: CallbackQuery):
    await callback.message.edit_text(text.about, parse_mode=ParseMode.HTML, reply_markup=but.back)


@dp.callback_query(F.data == 'perevag')
async def cmd_asd(callback: CallbackQuery):
    await callback.message.edit_text(text.perevag, reply_markup=but.back)


@dp.callback_query(F.data == 'channel')
async def cmd_heart(callback: CallbackQuery):
    await callback.message.edit_text("""Щоб знати найсвіжіші новини та бачити статистику знищених ворожих сил, рекомендуємо підписатися на наш телеграм канал.
Посилання: https://t.me/feniksdpsu""", reply_markup=but.back)


@dp.callback_query(F.data == 'back')
async def cmd_start(callback: CallbackQuery):
    await callback.message.edit_text("""Твоя сила — наша перевага!
Вітаємо в боті полку Phoenix. Заповни анкету, переглянь вакансії та зроби перший крок до служби в одному з найефективніших підрозділів ДПСУ.""",
                                     reply_markup=but.main_inline)

class RecruitingForm(StatesGroup):
    PIB = State()
    birth = State()
    phone = State()
    city = State()
    posada = State()
    komentar = State()


import smtplib
from email.mime.text import MIMEText

async def send_anketa_email(data):
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    sender_email = "fenixdpsumail@gmail.com"  # твоя почта-отправитель
    app_password = "pvca hwnj vuye xijg"       # твой пароль приложения
    recipient_email = "prikksrfeniks@gmail.com"    # получатель анкеты

    # Текст письма
    subject = "Нова анкета"
    body = (
        f"📥 Нова анкета:\n\n"
        f"👤 Прізвище, ім'я, по-батькові: {data['PIB']}\n"
        f"🗓 Дата народження: {data['birth']}\n"
        f"📞 Номер телефону: {data['phone']}\n"
        f"🏙 Місто: {data['city']}\n"
        f"💼 Посада: {data['posada']}\n"
        f"💬 Коментар: {data['komentar']}\n"
    )

    msg = MIMEText(body, "plain", "utf-8")
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = recipient_email

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, app_password)
        server.sendmail(sender_email, recipient_email, msg.as_string())
        server.quit()
        print("Письмо успешно отправлено")
    except Exception as e:
        print(f"Ошибка при отправке письма: {e}")




@dp.callback_query(F.data == 'anketa')
async def cmd_anketa(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer("""📑 Анкета

Надайте відповідь на наступні запитання 👇""")
    await callback.message.answer("Прізвище ім'я по-батькові")
    await state.set_state(RecruitingForm.PIB)





@dp.message(RecruitingForm.PIB)
async def cmd_pib(message: Message, state: FSMContext):
    await state.update_data(PIB=message.text)
    await message.answer("""🗓 Дата народження

ℹ️ у форматі дд-мм-рррр


ЗВЕРНІТЬ УВАГУ!!! 
Вам має бути 18+ років щоб далі заповнити анкету
Приклад: 12-12-2000""")
    await state.set_state(RecruitingForm.birth)


def is_valid_birthdate(date_text: str) -> bool:
    try:
        birth_date = datetime.datetime.strptime(date_text, "%d-%m-%Y")
        today = datetime.datetime.today()
        age = (today - birth_date).days // 365
        return age >= 18
    except ValueError:
        return False


@dp.message(RecruitingForm.birth)
async def cmd_birth(message: Message, state: FSMContext):
    if not is_valid_birthdate(message.text):
        await message.answer("""Введіть правильну дату народження за форматом 12-12-2000
        Вам має бути більше 18 років щоб продовжити""")

        return

    await state.update_data(birth=message.text)
    kb = ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text="📲 Поділитися контактом", request_contact=True)]],
        resize_keyboard=True,
        one_time_keyboard=True
    )
    await message.answer(
        """📱 Номер телефону

ℹ️ натисніть кнопку нижче, щоб поділитися номером телефону, або введіть його у міжнародному форматі +380ХХХХХХХХХ 👇""",
        reply_markup=kb
    )
    await state.set_state(RecruitingForm.phone)


def is_valid_phone(phone: str) -> bool:
    return re.match(r'^\+?\d{10,15}$', phone)


@dp.message(RecruitingForm.phone)
async def cmd_phone(message: Message, state: FSMContext):
    # Перевірка: контакт або текст
    if not is_valid_phone(message.text):
        await message.answer("Увведений некорректний номер телефону. Спробуйте ще раз ")
        return
    phone_number = message.contact.phone_number if message.contact else message.text
    await state.update_data(phone=phone_number)
    await message.answer("🗺 Місто фактичного перебування\n\nℹ️ назва населеного пункта",
                         reply_markup=ReplyKeyboardRemove())
    await state.set_state(RecruitingForm.city)


@dp.message(RecruitingForm.city)
async def cmd_city(message: Message, state: FSMContext):
    await state.update_data(city=message.text)
    await message.answer("""📋 Бажана посада

ℹ️ оберіть за допомогою кнопок 👇""", reply_markup=but.reply_pos)
    await state.set_state(RecruitingForm.posada)


@dp.message(RecruitingForm.posada)
async def cmd_posada(message: Message, state: FSMContext):
    await state.update_data(posada=message.text)
    await message.answer("""💬 Коментар

ℹ️ напишіть коментар, якщо бажаєте, або поставте -""", reply_markup=ReplyKeyboardRemove())
    await state.set_state(RecruitingForm.komentar)


@dp.message(RecruitingForm.komentar)
async def cmd_komentar(message: Message, state: FSMContext):
    await state.update_data(komentar=message.text)
    data = await state.get_data()
    await send_anketa_email(data)

    await message.answer("✅ Дякуємо! Вашу анкету надіслано на пошту.")
    await state.clear()

    data = await state.get_data()
    user_data_message = (
        f"📥 Нова анкета:\n\n"
        f"👤 Прізвище, ім'я, по-батькові: {data['PIB']}\n"
        f"🗓 Дата народження: {data['birth']}\n"
        f"📞 Номер телефону: {data['phone']}\n"
        f"🏙 Місто: {data['city']}\n"
        f"💼 Посада: {data['posada']}\n"
        f"💬 Коментар: {data['komentar']}\n"
    )

    await message.answer("✅ Дякуємо! Вашу анкету надіслано. Очікуйте на відповідь.", reply_markup=but.main_inline)
    await send_anketa_email(data)  # сначала отправляем
    await state.clear()  # потом чистим состояние





############################################ВАКАНСИИ!!!!!!###################################################################

@dp.callback_query(F.data == '')
async def cmd_heart(callback: CallbackQuery):
    await callback.message.edit_text(text.technik, reply_markup=but.inline)


@dp.callback_query(F.data == 'inzhenerbpla')
async def inzhenerbpla_handler(callback: CallbackQuery):
    await callback.message.edit_text(text.bpla_inj, reply_markup=but.back)


@dp.callback_query(F.data == 'tekhnikbpla')
async def tekhnikbpla_handler(callback: CallbackQuery):
    await callback.message.edit_text(text.technik, reply_markup=but.back)


@dp.callback_query(F.data == 'vodiybpla')
async def vodiybpla_handler(callback: CallbackQuery):
    await callback.message.edit_text(text.vodiy, reply_markup=but.back)


@dp.callback_query(F.data == 'saperbpla')
async def saperbpla_handler(callback: CallbackQuery):
    await callback.message.edit_text(text.saper, reply_markup=but.back)


@dp.callback_query(F.data == 'medyk')
async def medyk_handler(callback: CallbackQuery):
    await callback.message.edit_text(text.medik, reply_markup=but.back)


@dp.callback_query(F.data == 'rebrer')
async def rebrer_handler(callback: CallbackQuery):
    await callback.message.edit_text(text.operator_reb, reply_markup=but.back)


@dp.callback_query(F.data == 'vybuh')
async def vybuh_handler(callback: CallbackQuery):
    await callback.message.edit_text(text.babax_bpla, reply_markup=but.back)


@dp.callback_query(F.data == 'remont')
async def remont_handler(callback: CallbackQuery):
    await callback.message.edit_text(text.fix_bpla, reply_markup=but.back)


@dp.callback_query(F.data == 'dilovod')
async def dilovod_handler(callback: CallbackQuery):
    await callback.message.edit_text(text.dilovod, reply_markup=but.back)


@dp.callback_query(F.data == 'video')
async def video_handler(callback: CallbackQuery):
    await callback.message.edit_text(text.video, reply_markup=but.back)


@dp.callback_query(F.data == 'chergovyy')
async def chergovyy_handler(callback: CallbackQuery):
    await callback.message.edit_text(text.cherg, reply_markup=but.back)


@dp.callback_query(F.data == 'instruktor')
async def instruktor_handler(callback: CallbackQuery):
    await callback.message.edit_text(text.instruct_bpla, reply_markup=but.back)


@dp.callback_query(F.data == 'it')
async def it_handler(callback: CallbackQuery):
    await callback.message.edit_text(text.it, reply_markup=but.back)


@dp.callback_query(F.data == 'radio')
async def radio_handler(callback: CallbackQuery):
    await callback.message.edit_text(text.radio, reply_markup=but.back)


@dp.callback_query(F.data == 'psycholog')
async def psycholog_handler(callback: CallbackQuery):
    await callback.message.edit_text(text.psycho, reply_markup=but.back)


@dp.callback_query(F.data == 'poligrafolog')
async def poligrafolog_handler(callback: CallbackQuery):
    await callback.message.edit_text(text.poligraf, reply_markup=but.back)


@dp.callback_query(F.data == 'smm')
async def smm_handler(callback: CallbackQuery):
    await callback.message.edit_text(text.smm, reply_markup=but.back)


@dp.callback_query(F.data == 'finansyst')
async def finansyst_handler(callback: CallbackQuery):
    await callback.message.edit_text(text.finance, reply_markup=but.back)


@dp.callback_query(F.data == 'zakupivli')
async def zakupivli_handler(callback: CallbackQuery):
    await callback.message.edit_text(text.buy, reply_markup=but.back)


@dp.callback_query(F.data == 'dyzayner')
async def dyzayner_handler(callback: CallbackQuery):
    await callback.message.edit_text(text.graphic, reply_markup=but.back)


@dp.callback_query(F.data == 'back')
async def back_handler(callback: CallbackQuery):
    await callback.message.edit_text("Головне меню", reply_markup=but.main_inline)


# Запуск бота
async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот виключений')