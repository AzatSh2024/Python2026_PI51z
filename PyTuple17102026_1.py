#Кортежи. Задача 1
n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))

target = nums[-1]
found = False

for i in range(n - 1):
    for j in range(i + 1, n - 1):
        if nums[i] * nums[j] == target:
            found = True
            break
    if found:
        break

if found:
    print("ДА")
else:
    print("НЕТ")
