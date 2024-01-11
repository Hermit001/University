from collections import Counter

# Считываем количество строк
n = int(input())

# Инициализируем список для хранения слов
words = []

# Считываем слова из строк
for _ in range(n):
    line = input().split()
    words.extend(line)

# Используем Counter для подсчета количества каждого слова
word_counts = Counter(words)

# Сортируем слова по частоте встречаемости
sorted_word_counts = sorted(word_counts.items(), key=lambda x: (-x[1], x[0]))

# Выводим отсортированный список
for word, count in sorted_word_counts:
    print(word, count)
