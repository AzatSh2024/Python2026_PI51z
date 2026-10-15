# Множества. Задача 1
animals = set()
n = int(input("Введите количество: "))
for i in range(n):
    new_animal = input("Введите название животного №" + str(i+1) + ": ")
    animals.add(new_animal)
print(len(animals))