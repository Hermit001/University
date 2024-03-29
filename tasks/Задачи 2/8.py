# Считываем целое число N
N = int(input("Введите целое число от 1 до 365: "))

# Проверяем, что N находится в допустимом диапазоне
if 1 <= N <= 365:
    # Вычисляем номер дня недели для N-го дня
    day_of_week = (N + 3) % 7  # Добавляем 3, так как 1 января был четверг (четверг - это 3-й день недели)

    # Выводим результат, просто номер дня недели
    print("Номер дня недели для", N, "-го дня: ", day_of_week)
else:
    print("Ошибка: Введите целое число от 1 до 365.")