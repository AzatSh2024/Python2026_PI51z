# Строки как коллекция. Задача 20
name = input()

allowed = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"

for ch in name:
    if ch not in allowed:
        print(f"Неверный символ: {ch}")
        break
else:
    print("OK")
