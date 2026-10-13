#Задача 4 True и False. break и continue
count = 0
first_index = -1
line_number = 0

while True:
    line = input()
    if line == "СТОП":
        break   
    line_number += 1
    
    if "кот" in line or "Кот" in line:
        count += 1
        if first_index == -1:
            first_index = line_number
print(count)
print(first_index)
