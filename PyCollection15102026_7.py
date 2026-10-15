# Строки как коллекция. Задача 7
s = input()
codes = []
for ch in s:
    code = ord(ch)
    codes.append(str(code))

print(", ".join(codes))
