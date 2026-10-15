# Множества. Задача 2
cities = set()
n = int(input("Введите количество: "))
for i in range(n):
    cities.add(input("Введите город: "))
new_city = input("Введите город: ")
if new_city in cities:
    print("TRY ANOTHER")
else:
    print("OK")