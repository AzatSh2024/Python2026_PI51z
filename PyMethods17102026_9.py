# Методы списков и строк. Задача 9
letter = input().lower()
text = input()
result = []
for word in text.split():
    if letter in word.lower():
        result.append(word)

print(' '.join(result))
