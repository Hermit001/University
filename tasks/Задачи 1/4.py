# Считываем целое число от пользователя
num = int(input("Введите целое число: "))

# Вычисляем следующее и предыдущее числа
next_num = num + 1
previous_num = num - 1

# Выводим результат
print(f"Следующее число для числа {num}: {next_num}")
print(f"Предыдущее число для числа {num}: {previous_num}")