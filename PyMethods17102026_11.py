# Методы списков и строк. Задача 11
n = int(input())
results = []

for _ in range(n):
    nums = list(map(int, input().split()))
    if len(nums) == len(set(nums)):
        results.append("ДА")
    else:
        results.append("НЕТ")

for res in results:
    print(res)
