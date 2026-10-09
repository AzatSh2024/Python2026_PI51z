#Задача 9
num = int(input("Введите целое число: "))
n = abs(num)
total = 0

while n > 0:
    digit = n % 10
    total += digit
    n //= 10
print(total)
