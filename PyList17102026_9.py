#Списки. Задача 9
whitelist = []
while True:
    line = input().strip()
    if line == '':
        break
    whitelist.append(line)

whitelist_set = set(whitelist)

results = []
while True:
    query = input().strip()
    if query == '':
        break
    if query in whitelist_set:
        results.append(query)

for r in results:
    print(r)
