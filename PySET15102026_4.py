# Множества. Задача 4
m = int(input())
english = set()
for _ in range(m):
    english.add(input())

n = int(input())
german = set()
for _ in range(n):
    german.add(input())
    
only_one = english ^ german
if only_one:
    print(len(only_one))
else:
    print("NO")
