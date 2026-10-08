#Задача 5
while True:
 password = input("Введите пароль: ")
 confirm_password = input("Повторите пароль: ")
 if len(password) < 8:
    print("Слишком короткий!")
 elif password != confirm_password:
     print("Пароли не совпадают!")
 else:
    print("OK")
 break