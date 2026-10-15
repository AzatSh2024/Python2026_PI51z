# Множества. Задача 3
list1 = set()
while True:
    line = input()
    if line == "":
        break
    list1.add(int(line))

list2 = set()
while True:
    line = input()
    if line == "":
        break
    list2.add(int(line))

common = list1 & list2
if common:
    print(*common)
else:
    print("EMPTY")
