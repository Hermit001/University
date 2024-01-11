# Считываем количество строк
n = int(input())

# Создаем пустой словарь для хранения количества вхождений слов
word_count = {}

# Считываем и обрабатываем каждую строку
for _ in range(n):
    words = input().split()
    for word in words:
        # Если слово уже есть в словаре, увеличиваем его счетчик
        if word in word_count:
            word_count[word] += 1
        # Если слова нет в словаре, создаем новую запись
        else:
            word_count[word] = 1

# Находим слово с максимальным количеством вхождений
max_count = max(word_count.values())

# Создаем список слов с максимальным количеством вхождений
max_words = [word for word, count in word_count.items() if count == max_count]

# Сортируем список слов в алфавитном порядке
max_words.sort()

# Выводим первое слово из списка (первое в алфавитном порядке)
print(max_words[0])
