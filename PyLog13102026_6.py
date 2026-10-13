#Задача 6 True и False. break и continue
total = 0
count = 0
found_step = -1

while True:
    num = int(input())
    if num == 0:
        break   
    count += 1
    total += num
    
    if total == 10 and found_step == -1:
        found_step = count

print(found_step)