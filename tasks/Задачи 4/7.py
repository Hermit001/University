# Считываем целое положительное число из четырех цифр с ввода пользователя
number = int(input("Введите целое положительное число из четырех цифр: "))

# Разбиваем число на отдельные цифры
digit1 = number // 1000  # Первая цифра (тысячи)
digit2 = (number // 100) % 10  # Вторая цифра (сотни)
digit3 = (number // 10) % 10  # Третья цифра (десятки)
digit4 = number % 10  # Четвертая цифра (единицы)

# Проверяем, является ли число палиндромом
if digit1 == digit4 and digit2 == digit3:
    print("Да")
else:
    print("Нет")