# Строки как коллекция. Задача 15
n = int(input())
s = input()

if len(s) > n:
    print(s[:n-3] + "...")
else:
    print(s)
