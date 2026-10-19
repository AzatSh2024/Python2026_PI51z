# Методы списков и строк. Задача 7
tokens = input().split()
stack = []

for token in tokens:
    if token in {'+', '-', '*', '/'}:
        # Извлекаем два последних числа из стека
        right = stack.pop()
        left = stack.pop()
        
        if token == '+':
            res = left + right
        elif token == '-':
            res = left - right
        elif token == '*':
            res = left * right
        elif token == '/':
            # В задачах такого типа обычно подразумевается целочисленное деление
            res = int(left / right)
        
        stack.append(res)
    else:
        # Если токен не оператор — это число
        stack.append(int(token))

print(stack[0])
