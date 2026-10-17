#Кортежи. Задача 2
n = int(input())
pairs = []

for _ in range(n):
    line = input().split()
    surname = line[0]
    grade = int(line[1])
    pairs.append((surname, grade))

for surname, grade in pairs:
    print(surname, grade)

print()

for surname, grade in pairs:
    if grade == 4 or grade == 5:
        print(surname, grade)
