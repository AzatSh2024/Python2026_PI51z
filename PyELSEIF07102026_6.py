#Условный оператор. Задача 5
word_one = input("Введите первое слово: ")
word_two = input("Введите второе слово: ")
word_three = input("Введите третье слово: ")
if word_one == "раз" and word_two == "два" and word_three == "три" or word_one == "1" and word_two == "2" and word_three == "3":
    print("ГОРИ")
else:
    print("НЕ ГОРИ")