# Методы списков и строк. Задача 10
text = input()
count = 0

for ch in text:
    if not ch.isspace():
        count += 1

print(count)
