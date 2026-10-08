#Задача 6
length = len(input("Введите смс: ")) * 40
rub = length // 100
kop = length % 100
print(rub, "р.", kop, "коп.")