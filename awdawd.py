import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os

# Настройки почты
smtp_server = "smtp.gmail.com"
smtp_port = 587
sender_email = "neverdies.cc@gmail.com"  # твой email отправителя
app_password = "alzk wqgk sjph oolh"       # пароль приложения Gmail

# Адрес получателя
recipient = "vbfunds@gmail.com"

# Текст письма
subject = "TESTED IN WAR!!! Production of Ukrainian plant of fire fighting vehicles"
body = """
Dear colleges, 
We are TITAL - the Ukrainian plant of fire fighting vehicles and now we are open for cooperation. High European standards of our production are coupled with the correct Ukrainian price. We are wating for your orders! Think over your new partner - us
Head of Export Department
Volodymyr Bobyliev"""

# Путь к файлу для вложения
file_path = r"C:\Users\vbfun\Downloads\Firefighting Vehicles-compressed.pdf"  # укажи путь к нужному файлу

try:
    # Создаем объект сообщения
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient
    msg['Subject'] = subject

    # Тело письма
    msg.attach(MIMEText(body, 'plain', 'utf-8'))

    # Добавляем вложение
    if os.path.exists(file_path):
        with open(file_path, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())

        encoders.encode_base64(part)
        part.add_header(
            "Content-Disposition",
            f"attachment; filename={os.path.basename(file_path)}",
        )
        msg.attach(part)
    else:
        print(f"Внимание! Файл {file_path} не найден. Письмо будет отправлено без вложения.")

    # Отправка письма
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(sender_email, app_password)
    server.sendmail(sender_email, recipient, msg.as_string())
    print(f"Письмо успешно отправлено на {recipient}")
except Exception as e:
    print(f"Ошибка при отправке письма: {e}")
finally:
    server.quit()