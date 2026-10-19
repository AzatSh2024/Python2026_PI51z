# Словари. Задача №3
n = int(input())
dictionary = {}

for _ in range(n):
    word, translation = input().split()
    dictionary[word] = translation

search_word = input()

if search_word in dictionary:
    print(dictionary[search_word])
else:
    print("Слово не найдено")
