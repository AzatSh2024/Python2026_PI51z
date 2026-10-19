# Словари. Задача №2
n = int(input())
result = []

for _ in range(n):
    name, grade = input().split()
    result.append(f"{name}: {grade}")

for line in result:
    print(line)
