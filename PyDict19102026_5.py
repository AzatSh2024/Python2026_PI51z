# Словари. Задача №5
n = int(input())
prices = {}

for _ in range(n):
    product, price = input().split()
    prices[product] = price

search_product = input()

if search_product in prices:
    print(prices[search_product])
else:
    print("Товар не найден")
