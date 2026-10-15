# Строки как коллекция. Задача 19
n = int(input())
result = []

for i in range(n):
    line = input()
    if line.startswith("####"):
        continue
    elif line.startswith("%%"):
        result.append(line[2:])
    else:
        result.append(line)
for r in result:
    print(r)
