n = int(input())
numbers = [int(input()) for _ in range(n)]
print(*(numbers[i] + numbers[i + 1] for i in range(n - 1)))
