# Методы split и join. Списочные выражения. Задача 8
url = input()
start = url.find('q=')
if start != -1:
    start += 2
    end = url.find('&', start)
    if end == -1:
        end = len(url)
    print(url[start:end])
else:
    print()

