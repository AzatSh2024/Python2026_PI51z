#Кортежи. Задача 6
n = int(input())
arr = []

for _ in range(n):
    arr.append(int(input()))

for i in range(n - 1):
    swapped = False
    for j in range(0, n - i - 1):
        if arr[j] > arr[j + 1]:
            # Меняем элементы местами
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            swapped = True
    if not swapped:
        break

for num in arr:
    print(num)
