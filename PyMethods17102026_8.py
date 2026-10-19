# Методы списков и строк. Задача 8
text = input().lower()

freq = {}
for ch in text:
    freq[ch] = freq.get(ch, 0) + 1

max_char = None
max_count = -1

for ch, count in freq.items():
    if count > max_count:
        max_count = count
        max_char = ch

print(max_char)
