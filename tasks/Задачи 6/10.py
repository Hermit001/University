# Считываем строку с ввода
input_string = input("Введите строку: ")

# Находим индекс первого вхождения буквы "h"
first_h_index = input_string.find("h")

# Находим индекс последнего вхождения буквы "h"
last_h_index = input_string.rfind("h")

# Если оба индекса найдены, то удаляем часть строки между ними
if first_h_index != -1 and last_h_index != -1:
    result_string = input_string[:first_h_index] + input_string[last_h_index + 1:]
else:
    result_string = input_string

# Выводим результат
print(result_string)
