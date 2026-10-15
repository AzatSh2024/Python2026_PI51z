# Множества. Задача 6
m = int(input())

k = int(input())
common_students = set()
for i in range(k):
    common_students.add(input().strip())

for i in range(m - 1):
    k = int(input())
    current_day = set()
    for _ in range(k):
        current_day.add(input().strip())
    common_students &= current_day

for name in common_students:
    print(name)
