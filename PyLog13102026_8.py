#Задача 8 True и False. break и continue
found_cat = False

while True:
    line = input()
    if line == "СТОП":
        break
    if "пёс" in line or "Пёс" in line:
        found_cat = False
        continue
    if "кот" in line or "Кот" in line:
        found_cat = True
if found_cat:
    print("МЯУ")
else:
    print("НЕТ")
