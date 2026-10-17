#Кортежи. Задача 4
n = int(input())
lines = [input() for _ in range(n)]
lines.sort(key=lambda x: (len(x), x))

for line in lines:
    print(line)
