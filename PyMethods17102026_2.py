# Методы списков и строк. Задача 2

words = input().split()
max_len = max(len(word) for word in words)
print(max_len)
