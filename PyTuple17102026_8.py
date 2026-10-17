#Кортежи. Задача 8
n = int(input())
results = []

for _ in range(n):
    a, b = map(int, input().split())
    if a > b:
        a, b = b, a
    results.append(f"{a} {b}")

print("\n".join(results))
