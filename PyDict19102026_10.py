# Словари. Задача №10
n = int(input())
dictionary = {}

for _ in range(n):
    original, translation = input().split()
    dictionary[original] = translation

text = input().split()
result = []

for word in text:
    if word in dictionary:
        result.append(dictionary[word])
    else:
        result.append(word)

print(" ".join(result))
