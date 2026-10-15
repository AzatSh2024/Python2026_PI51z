# Строки как коллекция. Задача 10
shift = int(input())
text = input()

alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
result = []

for ch in text:
    if ch in alphabet:
        idx = alphabet.index(ch)
        new_idx = (idx + shift) % 33
        result.append(alphabet[new_idx])
    else:
        result.append(ch)

print("".join(result))
