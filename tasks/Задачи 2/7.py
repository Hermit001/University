# Считываем год
year = input("Введите год: ")

# Проверяем, что введенное значение является целым положительным числом
if year.isdigit():
    year = int(year)
    if year > 0:
        # Вычисляем номер века
        century = (year - 1) // 100 + 1

        # Выводим результат
        print("Номер века:", century)
    else:
        print("Ошибка: Введите положительное число.")
else:
    print("Ошибка: Введите целое положительное число.")