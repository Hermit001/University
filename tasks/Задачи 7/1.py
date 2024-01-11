input_text = input("Введите текст: ")
words = input_text.split()
word_count = {}

counts = []

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 0
    counts.append(str(word_count[word]))

result = " ".join(counts)
print(result)