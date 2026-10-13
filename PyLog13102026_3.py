#Задача 3 True и False. break и continue
line_number = 0
found_index = -1

while True:
    line = input()
    if line == "СТОП":
        break
    line_number += 1
    if "кот" in line or "Кот" in line:
        found_index = line_number
print(found_index)
