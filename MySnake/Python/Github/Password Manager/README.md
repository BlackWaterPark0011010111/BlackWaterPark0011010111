
////////////////
RUS
/////////////////


Password Manager
Это небольшое консольное приложение для генерации, проверки и хранения паролей в зашифрованном виде.Он осуществляет  Генерация безопасных паролей,Проверка сложности пароля,Хеширование паролей перед сохранением,Сохранение паролей в JSON-файл,Проверка введённого пароля на совпадение с сохранённым.

Перед началом работы нам нужно установить зависимости:
Нам нужно установить bcrypt``` [pip install bcrypt]```- он используется для хеширования паролей.Он умеет делать пароли надёжными, 
так, что даже если кто-то получит доступ к passwords.json, он не сможет узнать реальные пароли. используеться и настраиваеться  для проверки сложности, например проверяет наличие заглавных букв, цифр, спецсимволов и определяет, соответствует ли пароль всем требованиям требованиям безопасности

Структура проекта
```
password_manager
│── main.py             # Здесь основной интерфейс и запуск кода
│── password_utils.py   # по проверке, генерация, хеширование паролей
│── storage.py          # Чтение и запись паролей в файл json
│── passwords.json      # Хранилище паролей (будет создаваться автоматическипри запуске кода)
│── README.md           # Описание что этот код делает
```
В main.py - происходит взаимодействие программы с пользователем , выбор всего меню и действий, также создание пароля, проверка просмотр и сам интерфейс строк
В этом файле происходит взаимодействие с пользователем:
Выбор действия (создание пароля, проверка, просмотр)
Обработка пользовательского ввода
Вызов функций для работы с паролями

В password_utils.py - здесб весь мезанизм, а именно как  работать с паролями, то есть:генерация пароля- мы  создаём случайный пароль из букв, цифр и спецсимволов. Мы проверяем насколько он сложный и успешный в своей комбинацииБ мы хешируем  его с использованием и с помощью bcrypt,и также ведем сравнение введенного пароля с созраненным.

В ```storage.py``` - мы работаем с файлом. Мы загружает пароли из passwords.json и созраняем новые в этот же файл



re используеться  для наличие заглавных букв, цифр, спецсимволов и определяет, соответствует ли пароль требованиям 
```import re

password = "StrongPass1!"
if re.search(r"[A-Z]", password) and re.search(r"\d", password):
    print("Password is safe!")
```





это для созранения паролей в passwords.json.
```import json

data = {"example.com": "hashed_password"}
with open("passwords.json", "w") as file:
    json.dump(data, file)```



////////////////
ENG
/////////////////
 
 Password Manager 
So, basically, this is a small console application for generating, checking, and storing passwords in, like, an encrypted way. Uh, it does things like:

Generating secure passwords
Checking password strength
Hashing passwords before saving them
Storing passwords in a JSON file
Checking if an entered password matches the stored one
🚀 1. Before You Start
Okay, so, before running the code, we need to install some stuff.

First, we install ```bcrypt```:

```pip install bcrypt```

Now, why do we even need bcrypt? Well, it's used for hashing passwords. Basically, it makes them super secure, like, even if someone gets access to passwords.json, they won’t be able to see the real passwords.and,we also use it to check password strength-like, does it have uppercase letters, numbers, special characters, and stuff like that?

Project Structure
so here's, like, how everything is organized:


```password_manager
│── main.py             # The main interface and where the code runs
│── password_utils.py   # Handles password checking, generation, and hashing
│── storage.py          # Reads and writes passwords to the JSON file
│── passwords.json      # Where passwords are stored (gets created automatically)
│── README.md           # this file, explaining what’s going on here```
🛠 How It Works?
main.py - The Interface Thing
This file, deals with the user. It’s where you pick actions from the menu, create passwords, check them, and, view stored ones.

What happens here:Choosing an action (create, check, or view passwords)Handling user inputCalling functions to do the actual password work

password_utils.py - The Brains of the Operation
This is where all the password magic happens. Like:
Generating passwords → It randomly creates a password using letters, numbers, and special characters.Checking password strength → It, makes sure your password is not weak.Hashing passwords → It encrypts them using bcrypt.Comparing passwords → It checks if a given password matches the stored (hashed) one.

storage.py - Saving & Loading Passwords
Here, we deal with the file where passwords are stored.

Loads passwords from passwords.json
Saves new passwords to passwords.json

Regex for Password Checking
We use regular expressions (re module) to check if a password has uppercase letters, numbers, and special characters.

Example:

```import re

password = "StrongPass1!"
if re.search(r"[A-Z]", password) and re.search(r"\d", password):
    print("Password is safe!")
📦 Saving Passwords in passwords.json
And passwords are stored in a JSON file like this:```

```
import json

data = {"example.com": "hashed_password"}
with open("passwords.json", "w") as file:
    json.dump(data, file)```
Final Thoughts
So, like, this Password Manager is a really useful thing. It keeps your passwords safe, hashes them, and lets you store them properly. Plus, it's, like, simple and easy to use. 