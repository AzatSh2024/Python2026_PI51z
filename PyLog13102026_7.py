#Задача 7 True и False. break и continue
n = int(input())
good_lines = []

for i in range(n):
    line = input()
    if "плохо" in line:
        continue
    good_lines.append(line)
for line in good_lines:
    print(line)
