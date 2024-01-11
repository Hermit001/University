# Считываем количество пар синонимов
n = int(input())

# Создаем пустой словарь для синонимов
synonyms = {}

# Считываем пары синонимов и заполняем словарь
for _ in range(n):
    pair = input().split()
    synonym1, synonym2 = pair[0], pair[1]
    synonyms[synonym1] = synonym2
    synonyms[synonym2] = synonym1

# Считываем искомый ключ
key = input()

# Проверяем, есть ли такой ключ в словаре синонимов, и если есть, выводим его синоним
if key in synonyms:
    print(synonyms[key])
else:
    print("Такого ключа нет в словаре синонимов")