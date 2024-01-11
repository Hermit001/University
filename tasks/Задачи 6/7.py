# Считываем строку с числами, разделенными пробелами
numbers_str = input("Введите строку чисел, разделенных пробелами: ")

# Разбиваем строку на список чисел
numbers = numbers_str.split()

# Создаем пустое множество для отслеживания уникальных чисел
unique_numbers = set()

# Проходим по числам в строке
for num in numbers:
    if num in unique_numbers:
        print("Да")
    else:
        print("Нет")
        unique_numbers.add(num)
