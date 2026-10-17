#Списки. Задача 10
n = int(input())
word = [''] * n

for _ in range(n):
    pos, letter = input().split()
    pos = int(pos)
    word[pos - 1] = letter

print(''.join(word))
