# Задание: "Словарь 3"

text = "footballcyberpunkextraterritorialityconversationalistblockophthalmoscopicinterdependencemamauserfff"

result = {}


for letter in text:
    if letter in result:
        result[letter] += 1
    else:
        result[letter] = 1


for value in result:
    print(f"{value}: {result[value]}")
