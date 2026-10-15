# Строки как коллекция. Задача 13
s = input()

if s.startswith("Не ") or s.startswith("не "):
    print(s[3:])
else:
    print(s)
