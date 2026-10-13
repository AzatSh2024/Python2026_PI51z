#Задача 9 True и False. break и continue
n = int(input())
total = 0

for i in range(n):
    num = int(input())
    if num <= 0:
        continue  # пропускаем неположительные числа
    total += num
print(total)
