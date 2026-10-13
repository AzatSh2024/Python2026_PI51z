#Задача 5 True и False. break и continue
a = int(input())
b = int(input())

result = []
for num in range(a, b + 1):
    if num % 3 == 0 and num % 5 == 0:
        result.append("FizzBuzz")
    elif num % 3 == 0:
        result.append("Fizz")
    elif num % 5 == 0:
        result.append("Buzz")
    else:
        result.append(str(num))

print(" ".join(result))
