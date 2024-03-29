# Считываем три целых числа с ввода пользователя
year = int(input("Введите год: "))
month = int(input("Введите месяц (от 1 до 12): "))
day = int(input("Введите день (от 1 до 31): "))

# Проверяем, что введенные данные находятся в допустимых диапазонах
if 1 <= month <= 12 and 1 <= day <= 31:
    # Определяем количество дней в текущем месяце (для невисокосного года)
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # Проверяем, что введенный день не превышает максимальное количество дней в месяце
    if day <= days_in_month[month - 1]:
        # Увеличиваем день на 1
        day += 1
        
        # Проверяем, нужно ли увеличивать месяц
        if day > days_in_month[month - 1]:
            day = 1
            month += 1
            # Проверяем, нужно ли увеличивать год
            if month > 12:
                month = 1
                year += 1  # Увеличиваем год на 1
        
        # Выводим дату следующего дня в формате день-месяц-год
        print(f"{day}-{month}-{year}")
    else:
        print("Ошибка: Введенный день превышает максимальное количество дней в месяце.")
else:
    print("Ошибка: Проверьте правильность введенных данных (месяц от 1 до 12, день от 1 до 31, год - целое число).")
2