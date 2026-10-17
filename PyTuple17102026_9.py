#Кортежи. Задача 9
n = int(input())
people = []

for _ in range(n):
    line = input().split()
    surname = line[0]
    height = int(line[1])
    people.append((height, surname))

people.sort(reverse=True)

for height, surname in people:
    print(f"{surname} {height}")
