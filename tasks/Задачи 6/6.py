# Считываем две строки с числами, разделенными пробелами
first_line = input("Введите первую строку чисел, разделенных пробелами: ")
second_line = input("Введите вторую строку чисел, разделенных пробелами: ")

# Разбиваем строки на списки чисел
first_nums = set(map(int, first_line.split()))
second_nums = set(map(int, second_line.split()))

# Находим пересечение множеств, чтобы найти числа, которые встречаются и в первой, и во второй строке
common_nums = first_nums.intersection(second_nums)

# Выводим результат на экран
print(*common_nums)
