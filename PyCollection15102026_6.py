# Строки как коллекция. Задача 6
word = input()
n = int(input())

if 1 <= n <= len(word):
    print(word[n - 1])
else:
    print("ОШИБКА")
