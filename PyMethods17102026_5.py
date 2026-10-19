# Методы списков и строк. Задача 5
n = int(input())
for _ in range(n):
    line = input()
    
    # Ищем позицию символа #
    hash_pos = line.find('#')
    
    if hash_pos != -1:
        # Если # есть — обрезаем строку до него
        line = line[:hash_pos]
    
    # Убираем пробелы и табуляции в конце строки
    line = line.rstrip()
    
    # Выводим строку, только если она не пустая
    if line:
        print(line)
