#Задача 10 True и False. break и continue
total = 0
count = 0
limit = False

while True:
    num = int(input())   
    if num == 0:
        break   
    count += 1
    total += num   
    if total > 100:
        limit = True
        print("СТОП")
        print(count)
        break
if not limit:
    print("ОК")
