# Считываем целое число с ввода пользователя
number = int(input("Введите целое число: "))

# Проверяем знак числа и выводим соответствующее значение
if number > 0:
    print("1")
elif number < 0:
    print("-1")
else:
    print("0")