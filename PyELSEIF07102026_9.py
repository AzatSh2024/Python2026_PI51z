#Условный оператор. Задача 9
login = input("Введите логин: ")
email = input("Введите e-mail: ")
if "@" in email and not "@" in login:
    print("ОК")
else:
    print("ОШИБКА")