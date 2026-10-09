n = int(input("Введите число: "))
x = 1
notzero = False
for i in range(n):
    num = int(input())
    if num != 0:
        x *= num
        notzero = True
if not notzero:
    print(0)
else:
    print(x)
