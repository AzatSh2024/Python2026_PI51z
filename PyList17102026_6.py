#Списки. Задача 6
n = int(input())
numbers = []
for _ in range(n):
    numbers.append(int(input()))

p = int(input())
q = int(input())

total = sum(numbers[p:q+1])
print(total)
