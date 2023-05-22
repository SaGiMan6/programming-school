# Задание: "Словарь 3"

from string import punctuation


words = input().lower().translate(str.maketrans("", "", punctuation)).split()

frequency = {}

cur = ""
min = len(words) + 1


for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1


for value in sorted(frequency):
    if frequency[value] < min:
        cur = value
        min = frequency[value]


print(cur)
