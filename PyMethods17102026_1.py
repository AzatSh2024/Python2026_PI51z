# Методы списков и строк. Задача 1
n = int(input())
results = []

for i in range(n):
    s = input()
    pos = s.find('кот')
    if pos != -1:
        results.append((i + 1, pos + 1))

for line_num, pos_num in results:
    print(line_num, pos_num)
