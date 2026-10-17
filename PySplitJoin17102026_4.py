# Методы split и join. Списочные выражения. Задача 4
nums = list(map(int, input().split()))
result = [x**2 for x in nums if x % 2 != 0 and (x**2) % 10 != 9]
print(*result)
