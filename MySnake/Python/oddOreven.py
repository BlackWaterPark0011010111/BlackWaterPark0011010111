def check_string_length(s):
    if len(s) % 2 == 0:
        return "even"
    else:
        return "odd"

# Примеры использования
print(check_string_length("hello world"))  # Вывод: "odd"
print(check_string_length("hello planet")) # Вывод: "even"
print(check_string_length(""))  