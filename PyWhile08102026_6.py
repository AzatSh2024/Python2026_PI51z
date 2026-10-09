#Задача 6
while True:
    password = input("Введите пароль: ")
    confirm_password = input("Повторите пароль: ")

    if len(password) < 8:
        print("Слишком короткий!")
        continue
    elif "123" in password:
        print("Содержит 123!")
        continue
    elif password != confirm_password:
        print("Пароли не совпадают!")
        continue
    else:
        print("OK")
        break