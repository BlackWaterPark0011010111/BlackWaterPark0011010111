#import logging
#import smtplib
#from email.mime.text import MIMEText
#import sqlite3
#import os
#import sys
#from custom_handler import CustomHandler
#
#
#sys.stdout.reconfigure(encoding='utf-8')
#logging.basicConfig(
#    filename="app.log",
#    filemode="w",
#    encoding="utf-8",
#    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
#    level=logging.DEBUG
#)
#
#logger = logging.getLogger(__name__)
#
#logger.info("Приложение запущено")
#
#
#handler = logging.StreamHandler(sys.stdout)
#
#handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
#handler.stream.reconfigure(encoding='utf-8')  # ВАЖНО
#logger.addHandler(handler)
#logger.setLevel(logging.DEBUG)
#
#class CustomHandler(logging.Handler):
#    def emit(self, record):
#        log_entry = self.format(record)
#        
#        # Логика для обработки ошибок
#        print(f'Пользовательский обработчик: {log_entry}')
#        
#        # Если это ошибка или критическая ошибка
#        if record.levelname == 'ERROR' or record.levelname == 'CRITICAL':
#            print(f"ОШИБКА: {log_entry}")
#            self.send_email_notification(log_entry)
#            self.save_to_database(log_entry)
#    
#    def send_email_notification(self, log_entry):
#        # Настройки SMTP для отправки email
#        sender_email = "your_email@example.com"
#        receiver_email = "receiver_email@example.com"
#        password = os.getenv("EMAIL_PASSWORD")
#        
#        # Создание сообщения
#        subject = "Critical Error Notification"
#        body = f"A critical error occurred:\n\n{log_entry}"
#        msg = MIMEText(body)
#        msg['Subject'] = subject
#        msg['From'] = sender_email
#        msg['To'] = receiver_email
#        
#        # Отправка email
#        try:
#            with smtplib.SMTP('smtp.gmail.com', 587) as server:
#                server.starttls()
#                server.login(sender_email, password)
#                server.sendmail(sender_email, receiver_email, msg.as_string())
#            print("Email отправлен успешно.")
#        except Exception as e:
#            print(f"Ошибка при отправке email: {e}")
#
#    def save_to_database(self, log_entry):
#        
#        conn = sqlite3.connect('logs.db')
#        c = conn.cursor()
#        
#        
#        c.execute('''CREATE TABLE IF NOT EXISTS logs
#                     (levelname TEXT, message TEXT, created_at TIMESTAMP)''')
#        
#        # Вставка логов в таблицу
#        log_parts = log_entry.split(' - ')
#        level = log_parts[1] if len(log_parts) > 1 else 'UNKNOWN'
#        message = log_entry
#
#        c.execute("INSERT INTO logs (levelname, message, created_at) VALUES (?, ?, datetime('now'))", (level, message))
#
#
#        conn.commit()
#        conn.close()
#        print("Лог записан в базу данных.")