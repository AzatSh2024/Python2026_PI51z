#Задача 2
result = []
while True:
    num = input("Введите число: ")
    if num =="0":
        break
    result.append(num)
print(*result)