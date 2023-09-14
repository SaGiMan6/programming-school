# Задание: "Словарь 3"

indentifiers = input().split()

frequency = {}


for num, value in enumerate(indentifiers):
    if value in frequency:
        indentifiers[num] = f"{value}_{frequency[value]}"
        frequency[value] += 1
    else:
        frequency[value] = 1


print(*indentifiers)