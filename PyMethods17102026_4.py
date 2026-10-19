# Методы списков и строк. Задача 4

nums = list(map(int, input().split()))
p, q = map(int, input().split())
result = sum(x * x for x in nums[p:q+1])
print(result)
