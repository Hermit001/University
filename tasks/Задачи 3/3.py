# Считываем строку с вводом пользователя
input_string = input("Введите строку: ")

# Ищем позицию первого вхождения 'f' в строку
first_f_position = input_string.find('f')

# Если 'f' не найдено, выводим -1
if first_f_position == -1:
    print("-1")
else:
    # Ищем позицию последнего вхождения 'f' в строку
    last_f_position = input_string.rfind('f')

    # Выводим позиции, учитывая, что позиции начинаются с 0
    print(first_f_position, last_f_position)