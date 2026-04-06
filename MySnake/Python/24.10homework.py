#Проверьте входные учетные данные пользователя. 
#Вам следует распечатать сообщение, Welcome, {username}!если учетные данные действительны, и сообщение,
#Credentials are invalid если они недействительны.
#Используйте следующий код:


# username = input("What is your username? ")
# password = input(f"Type the password for username {username}: ")
# valid = {"username": "admin", "password": "admin"}

# if username=="admin" and password=="admin":
#    print(f'Welcome {username}')
# else:
#    print('Credentials are invalid ')
    


#     Определите функцию с именем isweekend, которая принимает параметр с именем dateтипа Datetime(со значением по умолчанию datetime.datetime.now()).

# Эта функция будет служить логическим выражением и вернет результат, Trueесли день недели в dateсубботе или воскресенье. FalseВ любом другом случае оно вернется .

# # На самом деле это можно сделать разными способами, но в этом упражнении вам потребуется использовать оператор ИЛИ .

# #Используйте следующие тестовые примеры:
# import datetime

# def isweekend(date= datetime.datetime.now()):
#     daynumber = date.weekday()
#     if daynumber == 5 or daynumber ==6:
#         return True
#     else:
#         return False

# print(isweekend(datetime.date(2021, 8, 6)))
# print(isweekend(datetime.date(2021, 8, 7)))
# print(isweekend(datetime.date(2021, 8, 8)))
# print(isweekend(datetime.date(2021, 8, 9)))

# username = input("What is your username? ")
# password = input(f"Type the password for username {username}: ")
# valid = {"username": "admin", "password": "admin"}
# today=datetime.date(2021, 8, 6)
# if isweekend (today):
#     print(f'Welcome {username}')
# else:
#     if username=="admin" and password=="admin":
#         print(f'Welcome {username}')
#     else:
#         print('Credentials are invalid ')



users = [
    {
        "name": "Holly",
        "password": "hunter"
    },
    {
        "name": "Peter",
        "password": "pan"
    },
    {
        "name": "Janis",
        "password": "joplin"
    }
]
def get_user( username, password):
    
    for user in users:
        if user["name"] == str(username) and user["password"] == str(password):
           return username
        
            



username = input("What is your username? ")
password = input(f"Type the password for username {username}: ")
result = get_user(username, password)
if result:
    print(result)
else:
    print('Error')