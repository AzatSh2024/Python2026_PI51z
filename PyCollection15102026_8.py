# Строки как коллекция. Задача 8
prev_word = input()

while True:
    curr_word = input()
    if curr_word[0] != prev_word[-1]:
        print(curr_word)
        break
    prev_word = curr_word
