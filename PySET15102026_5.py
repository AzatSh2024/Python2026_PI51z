# Множества. Задача 5
m = int(input())
library = set()
for _ in range(m):
    library.add(input().strip())

n = int(input())
results = []
for i in range(n):
    book = input().strip()
    if book in library:
        results.append("YES")
    else:
        results.append("NO")

for res in results:
    print(res)
