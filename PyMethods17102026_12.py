# Методы списков и строк. Задача 12
s = input()

if not s:
    print(0)
else:
    max_len = 1
    cur_len = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            cur_len += 1
        else:
            if cur_len > max_len:
                max_len = cur_len
            cur_len = 1

    if cur_len > max_len:
        max_len = cur_len

    print(max_len)
