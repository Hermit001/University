# Считываем целое положительное число N с ввода пользователя
N = int(input("Введите целое положительное число N: "))

# Инициализируем начальные значения для чисел Фибоначчи
a, b = 0, 1
position = 1  # Порядковая позиция

# Пока текущее число меньше N, продолжаем генерацию чисел Фибоначчи
while a < N:
    a, b = b, a + b
    position += 1

# Проверяем, является ли число N числом Фибоначчи
if a == N:
    print(position-1)
else:
    print(-1)