#Списки. Задача 2
n = int(input())
lines = []
for _ in range(n):
    lines.append(input())

query = input()

for line in lines:
    if query in line:
        print(line)
