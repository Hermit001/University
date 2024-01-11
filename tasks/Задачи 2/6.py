# Считываем вещественное число
number = input("Введите вещественное положительное число: ")

# Проверяем, что введенная строка содержит точку и состоит только из цифр
if "." in number and number.replace(".", "", 1).isdigit():
    # Находим индекс точки и извлекаем первую цифру справа
    dot_index = number.index(".")
    digit_after_dot = number[dot_index + 1]

    # Выводим результат
    print("Первая цифра справа после точки:", digit_after_dot)
else:
    print("Ошибка: Введите вещественное положительное число.")