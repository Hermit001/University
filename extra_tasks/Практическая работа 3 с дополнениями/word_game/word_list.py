import random

def load_word_list(file_path="words.txt"):
    # Загрузка списка слов из файла
    with open(file_path, "r") as file:
        words = file.read().split()
    return words

def select_random_word(words):
    # Выбор случайного слова из списка
    return random.choice(words)
