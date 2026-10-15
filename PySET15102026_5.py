# Множества. Задача 5
m = int(input())
library = set()
for i in range(m):
    library.add(input())

n = int(input())
for _ in range(n):
    book = input()
    if book in library:
        print("YES")
    else:
        print("NO")
