#Кортежи. Задача 10
n = int(input())
result = []

for _ in range(n):
    s = input()
    result.append((len(s), s))

for item in result:
    print(item)
