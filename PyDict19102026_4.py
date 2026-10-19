# Словари. Задача №4
text = input()
counts = {}

for ch in text:
    if ch == ' ':
        continue
    if ch not in counts:
        counts[ch] = 0
    counts[ch] += 1

max_count = -1
result_char = ''

for ch in text:
    if ch == ' ':
        continue
    if counts[ch] > max_count:
        max_count = counts[ch]
        result_char = ch

print(result_char)
