# Строки как коллекция. Задача 17
word1 = input()
word2 = input()

bulls = 0
cows = 0

used_in_bulls = [False] * len(word1)

for i in range(len(word1)):
    if word1[i] == word2[i]:
        bulls += 1
        used_in_bulls[i] = True

freq1 = {}
freq2 = {}

for i in range(len(word1)):
    if not used_in_bulls[i]:
        ch1 = word1[i]
        ch2 = word2[i]
        
        if ch1 in freq1:
            freq1[ch1] += 1
        else:
            freq1[ch1] = 1
            
        if ch2 in freq2:
            freq2[ch2] += 1
        else:
            freq2[ch2] = 1

for ch in freq1:
    if ch in freq2:
        cows += min(freq1[ch], freq2[ch])

print(f"Быки: {bulls}")
print(f"Коровы: {cows}")
