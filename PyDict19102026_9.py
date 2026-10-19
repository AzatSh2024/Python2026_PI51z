# Словари. Задача №9
n = int(input())
best_name = ""
best_grade = -1

for _ in range(n):
    name, grade_str = input().split()
    grade = int(grade_str)
    
    if grade > best_grade:
        best_grade = grade
        best_name = name

print(best_name)
