#Задача 10
a = int(input())  # первое число
b = int(input())  # второе число
op = input().strip()  # операция
if op == '+':
    print(a + b)
elif op == '-':
    print(a - b)
elif op == '*':
    print(a * b)
elif op == '/':
    if b == 0:
        print("ОШИБКА")
    else:
        print(a / b)
else:
    print("ОШИБКА")