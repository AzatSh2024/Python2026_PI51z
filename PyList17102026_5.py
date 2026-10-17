#Списки. Задача 5
n = int(input())
result = []
for _ in range(n):
    num = int(input())
    result.append(num * 3)

print(*result)
