# Методы split и join. Списочные выражения. Задача 6
n = int(input())
lines = [input() for _ in range(n)]
filtered = [line for line in lines if 'лук' not in line]
print(', '.join(filtered))
