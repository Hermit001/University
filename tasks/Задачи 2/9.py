# Считываем входные данные как строку
input_str = input("Введите количество минут после полуночи: ")

# Проверяем, является ли введенная строка целым числом
if input_str.isdigit():
    N = int(input_str)  # Преобразуем строку в целое число
    # Вычисляем количество часов и минут
    hours = N // 60
    minutes = N % 60

    # Выводим результат в формате "часы:минуты"
    print(f"{hours}:{minutes:02}")
else:
    print("Ошибка: Введите целое число минут после полуночи.")