# Считываем целое число с ввода пользователя
number = int(input("Введите целое число: "))

# Преобразуем число в строку и проверяем длину строки
if len(str(number)) == 3:
    print("Да")
else:
    print("Нет")