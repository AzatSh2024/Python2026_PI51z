#Кортежи. Задача 3
n = int(input())
lines = []

for _ in range(n):
    lines.append(input())
sorted_lines = sorted(lines)

for line in sorted_lines:
    print(line)
