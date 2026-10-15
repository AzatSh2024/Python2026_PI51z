# Строки как коллекция. Задача 9
s = input().lower()
vowels = "аеёиоуыэюя"
count = 0

for ch in s:
    if ch in vowels:
        count += 1
print(count)
