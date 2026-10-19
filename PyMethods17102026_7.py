# Методы списков и строк. Задача 7
tokens = input().split()
stack = []

for token in tokens:
    if token in {'+', '-', '*', '/'}:
        right = stack.pop()
        left = stack.pop()
        
        if token == '+':
            res = left + right
        elif token == '-':
            res = left - right
        elif token == '*':
            res = left * right
        elif token == '/':
            res = int(left / right)
        
        stack.append(res)
    else:
        stack.append(int(token))

print(stack[0])
