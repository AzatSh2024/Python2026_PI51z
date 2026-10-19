# Методы списков и строк. Задача 3

nums = list(map(int, input().split()))
p, q = map(int, input().split())
result = sum(nums[p:q+1])
print(result)
