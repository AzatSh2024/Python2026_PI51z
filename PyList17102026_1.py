#Списки. Задача 1
n = int(input())
words = []
for _ in range(n):
    words.append(input())
print(*words)
