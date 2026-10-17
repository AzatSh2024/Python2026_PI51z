#Списки. Задача 7
n = int(input())
lines = [input() for _ in range(n)]

word1 = input()
word2 = input()

for line in lines:
    if word1 in line and word2 in line:
        print(line)
