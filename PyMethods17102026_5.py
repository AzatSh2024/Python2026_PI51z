# Методы списков и строк. Задача 5
n = int(input())
clean_lines = []

for _ in range(n):
    s = input()
    
    hash_pos = s.find('#')
    if hash_pos != -1:
        s = s[:hash_pos]
    
    s = s.rstrip()
    
    if s:
        clean_lines.append(s)

for line in clean_lines:
    print(line)
