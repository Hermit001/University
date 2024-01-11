# Считываем первую метку времени
hours1 = int(input("Введите количество часов (первая метка времени): "))
minutes1 = int(input("Введите количество минут (первая метка времени): "))
seconds1 = int(input("Введите количество секунд (первая метка времени): "))

# Считываем вторую метку времени
hours2 = int(input("Введите количество часов (вторая метка времени): "))
minutes2 = int(input("Введите количество минут (вторая метка времени): "))
seconds2 = int(input("Введите количество секунд (вторая метка времени): "))

if hours1 > hours2 or (hours1 == hours2 and (minutes1 > minutes2 or (minutes1 == minutes2 and seconds1 > seconds2))):
    print("Ошибка: Первая метка времени не может быть позже второй.")
else:
    # Вычисляем разницу в секундах
    total_seconds1 = hours1 * 3600 + minutes1 * 60 + seconds1
    total_seconds2 = hours2 * 3600 + minutes2 * 60 + seconds2
    difference_seconds = total_seconds2 - total_seconds1

    # Выводим результат
    print("Разница в секундах:", difference_seconds)