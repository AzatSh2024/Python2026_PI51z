# Словари. Задача №6
n = int(input())
scores = {}
order = []

for _ in range(n):
    name, grade = input().split()
    grade = int(grade)
    
    if name not in scores:
        scores[name] = 0
        order.append(name)
    
    scores[name] += grade

for name in order:
    print(f"{name}: {scores[name]}")
