#Списки. Задача 4
n = int(input())
lines = []
for _ in range(n):
    lines.append(input())

for line in reversed(lines):
    print(line)
