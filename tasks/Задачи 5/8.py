# Инициализируем переменные для подсчета текущей длины и максимальной длины фрагмента
current_length = 1
max_length = 1

# Считываем первое число из последовательности
previous_number = int(input("Введите первое число (0 для завершения): "))

# Считываем остальные числа и проверяем, если последовательность закончена (0), то выходим из цикла
while True:
    number = int(input("Введите следующее число (0 для завершения): "))
    if number == 0:
        break
    if number == previous_number:
        current_length += 1
    else:
        current_length = 1
    if current_length > max_length:
        max_length = current_length
    previous_number = number

# Выводим максимальную длину фрагмента
print("Длина самого широкого фрагмента, где все элементы равны друг другу:", max_length)
