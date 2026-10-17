#Кортежи. Задача 7
n = int(input())
nums = []

for _ in range(n):
    nums.append(int(input()))

unique_nums = list(set(nums))
print(len(unique_nums))
