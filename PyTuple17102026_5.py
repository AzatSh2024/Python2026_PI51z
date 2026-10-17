#Кортежи. Задача 5
n = int(input())

if n <= 0:
    pass
elif n == 1:
    print(1)
else:
    fib = [1, 1]
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])

    for num in fib:
        print(num)
