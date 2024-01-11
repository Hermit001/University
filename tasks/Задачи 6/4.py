# Считываем строку и разбиваем ее на список целых чисел
lst = [int(s) for s in input("Введите строку чисел, разделенных пробелами: ").split()]

# Находим минимальное и максимальное числа и их индексы в списке
min_num = min(lst)
max_num = max(lst)
min_index = lst.index(min_num)
max_index = lst.index(max_num)

# Меняем местами минимальное и максимальное число
lst[min_index], lst[max_index] = lst[max_index], lst[min_index]

# Печатаем получившийся список
for num in lst:
    print(num, end=" ")
