#Задача 2 True и False. break и continue
count = int(input("Количество слов: "))
cat_is = False

for i in range(count):
    text = input()
    if 'кот' in text or 'Кот' in text:
        cat_is = True
        break
if cat_is:
        print("МЯУ")
else:
        print("НЕТ")
