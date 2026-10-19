# Словари. Задача №1
word = input()
counts = {}

for letter in word:
    if letter not in counts:
        counts[letter] = 0
    counts[letter] += 1

for letter in word:
    if counts[letter] is not None:
        print(f"{letter}: {counts[letter]}")
        counts[letter] = None
