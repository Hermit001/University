# Считываем количество строк
n = int(input())

# Создаем словарь для хранения стран и их городов
country_cities = {}

# Считываем информацию о странах и городах
for _ in range(n):
    line = input().split()
    country = line[0]
    cities = line[1:]
    for city in cities:
        country_cities[city] = country

# Считываем количество городов
m = int(input())

# Создаем список для хранения ответов
answers = []

# Считываем города и находим соответствующие страны
for _ in range(m):
    city = input()
    if city in country_cities:
        answers.append(country_cities[city])
    else:
        answers.append("Unknown")

# Выводим все ответы
for answer in answers:
    print(answer)
