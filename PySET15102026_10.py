# Множества. Задача 10

line1 = input().strip()
line2 = input().strip()
set1 = set()
if line1:
    parts1 = line1.split()
    for p in parts1:
        set1.add(int(p))

set2 = set()
if line2:
    parts2 = line2.split()
    for p in parts2:
        set2.add(int(p))

diff = set1 ^ set2

if diff:
    sorted_diff = sorted(diff)
    result = ""
    for x in sorted_diff:
        result += str(x) + " "
    print(result.strip())
else:
    print("EMPTY")
