# Считываем количество записей в словаре
n = int(input())

# Создаем пустой словарь для хранения результатов
results = {}

# Считываем и обрабатываем каждую запись
for _ in range(n):
    candidate, votes = input().split()
    votes = int(votes)
    
    # Если фамилия кандидата уже есть в словаре, добавляем голоса
    if candidate in results:
        results[candidate] += votes
    # Если фамилии нет в словаре, создаем новую запись
    else:
        results[candidate] = votes

# Сортируем фамилии кандидатов в алфавитном порядке
sorted_candidates = sorted(results.keys())

# Выводим результаты
for candidate in sorted_candidates:
    print(candidate, results[candidate])
