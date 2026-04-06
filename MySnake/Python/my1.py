import re
# Проверка корректности номера телефона
phone = input("Введите номер телефона: ")
pattern = r"^\+7\(\d{3}\)\d{3}-\d{2}-\d{2}$"

if re.match(pattern, phone):
    print("Номер корректен")
else:
    print("Некорректный номер")