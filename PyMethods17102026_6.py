# Методы списков и строк. Задача 6
text = input()
result_words = []

for word in text.split():
    robot_word = '-'.join(char.upper() for char in word)
    result_words.append(robot_word)

print(' '.join(result_words))
