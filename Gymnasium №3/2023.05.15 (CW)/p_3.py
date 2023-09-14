# Задание: "Словарь 3"

dict1 = {'a': 100, 'z': 333, 'b': 200, 'c': 300, 'd': 45, 'e': 98, 't': 76, 'q': 34, 'f': 90, 'm': 230}

dict2 = {'a': 300, 'b': 200, 'd': 400, 't': 777, 'c': 12, 'p': 123, 'w': 111, 'z': 666}

result = dict()


for value in dict1:
    if value in dict2:
        result[value] = dict1[value] + dict2[value]

        print(f"{value}: {result[value]}")
