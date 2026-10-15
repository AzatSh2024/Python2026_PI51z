# Множества. Задача 8
m = int(input())
fridge = set()
for i in range(m):
    fridge.add(input().strip())

n = int(input())
possible_recipes = []

for i in range(n):
    parts = input().strip().split()
    recipe_name = parts[0]
    ingredients = set(parts[1:])
    if ingredients <= fridge:
        possible_recipes.append(recipe_name)

for recipe in possible_recipes:
    print(recipe)
