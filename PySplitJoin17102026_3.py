# Методы split и join. Списочные выражения. Задача 3
n = int(input())
squares = [i ** 2 for i in range(n + 1)]
print(' '.join(str(x) for x in squares))
