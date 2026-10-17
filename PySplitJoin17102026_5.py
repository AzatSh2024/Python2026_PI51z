# Методы split и join. Списочные выражения. Задача 5

words = input().split()
result = '[' + ', '.join(f'"{w}"' for w in words) + ']'
print(result)
