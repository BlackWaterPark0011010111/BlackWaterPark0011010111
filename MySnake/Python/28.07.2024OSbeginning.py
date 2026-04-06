#https://github.com/P23-E06/python-basics-io-files-i-2024-BlackWaterPark0011010111/tree/main

#OS for beginning

with open(r"task1.txt", 'r', encoding='utf-8') as file:
    content = file.read()

# Печатаем содержимое файла
print(content)
print("-------------------------------------------")


# Определяем путь к файлу
file_path = 'task2.txt'

# Открываем файл и читаем его строки
with open(file_path, 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Количество строк минус две первые строки (заголовок и пустая строка)
task_count = len(lines) - 2

# Печатаем количество задач
print(task_count)

print("-------------------------------------------")


# Определяем путь к файлу
file_path = 'task3.txt'

# Открываем файл и читаем его строки
with open(file_path, 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Извлекаем строки с нечетными индексами (1, 3, 5, ...)
odd_lines = lines[0::2]

# Извлекаем строки с четными индексами (0, 2, 4, ...)
even_lines = lines[1::2]

# Печатаем сначала нечетные строки
for line in odd_lines:
    print(line, end='')

# Печатаем затем четные строки
for line in even_lines:
    print(line, end='')
print("-------------------------------------------")

# Открываем файл и читаем нужный фрагмент
file_path = 'task4.txt'

with open(file_path, 'r', encoding='utf-8') as file:
    file.seek(1622)  # Перемещаем указатель чтения на позицию 1622
    snippet = file.read(1634 - 1622 + 1)  # Читаем от позиции 1622 до 1634 включительно

print(snippet)


print("-------------------------------------------")

file_path = 'task5.txt'

with open(file_path, 'r', encoding='utf-8') as file:
    first_line = file.readline().rstrip('\n')  # Читаем первую строку и убираем символ переноса строки

# Подсчёт количества символов в строке без функции len()
char_count = 0
for char in first_line:
    char_count += 1

print(first_line)
print(char_count)

print("-------------------------------------------")

file_path = 'task6.txt'

# Инициализируем список для хранения количества символов в каждой строке
line_lengths = []

with open(file_path, 'r', encoding='utf-8') as file:
    for line in file:
        line = line.rstrip('\n')  # Убираем символ переноса строки
        count = 0
        for char in line:
            count += 1
        line_lengths.append(count)

print(line_lengths)

print("-------------------------------------------")

print("-------------------------------------------")