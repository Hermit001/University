# Считываем строку с ввода
input_string = input("Введите строку: ")

# Вычисляем середину строки
middle_index = len(input_string) // 2

# Разделяем строку на две части и меняем их местами
result_string = input_string[middle_index:] + input_string[:middle_index]

# Выводим результат
print(result_string)
