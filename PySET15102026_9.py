# Множества. Задача 9
m = int(input())
available = set()
for i in range(m):
    available.add(input().strip())

n = int(input())
cooked = set()

for i in range(n):
    day_dishes = input().strip().split()
    for dish in day_dishes:
        cooked.add(dish)
not_cooked = available - cooked

for dish in not_cooked:
    print(dish)
