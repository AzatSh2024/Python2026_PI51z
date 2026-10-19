# Словари. Задача №8
text = input().lower()
words = text.split()

counts = {}
order = []

for word in words:
    if word not in counts:
        counts[word] = 0
        order.append(word)
    counts[word] += 1

for word in order:
    print(f"{word}: {counts[word]}")
