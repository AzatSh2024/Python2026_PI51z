# Методы split и join. Списочные выражения. Задача 1
text = input()
words = text.split()
result = words[2::3]
print(' '.join(result))
