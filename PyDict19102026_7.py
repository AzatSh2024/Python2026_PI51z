# Словари. Задача №7
list1 = []
while True:
    line = input()
    if line == "":
        break
    list1.append(line)

list2 = []
while True:
    line = input()
    if line == "":
        break
    list2.append(line)

set2 = set(list2)

for word in list1:
    if word not in set2:
        print(word)
