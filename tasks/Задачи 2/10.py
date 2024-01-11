# Функция для считывания целого числа с проверкой
def read_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Ошибка: Введите целое число.")

# Считываем количество учеников в каждом классе
a = read_integer("Введите количество учеников в первом классе: ")
b = read_integer("Введите количество учеников во втором классе: ")
c = read_integer("Введите количество учеников в третьем классе: ")

# Вычисляем количество столов для каждого класса (каждый стол для двух учеников)
tables_for_a = (a + 1) // 2
tables_for_b = (b + 1) // 2
tables_for_c = (c + 1) // 2

# Вычисляем общее количество столов
total_tables = tables_for_a + tables_for_b + tables_for_c

# Выводим результат
print("Общее количество столов, которое нужно приобрести:", total_tables)