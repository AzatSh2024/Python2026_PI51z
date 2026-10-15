# Множества. Задача 7
n = int(input())

counts = {}
surnames_list = []

for i in range(n):
    surname = input().strip()
    surnames_list.append(surname)
    counts[surname] = counts.get(surname, 0) + 1

result = 0
seen = set()

for surname in surnames_list:
    if counts[surname] > 1 and surname not in seen:
        result += counts[surname]
        seen.add(surname)
print(result)
