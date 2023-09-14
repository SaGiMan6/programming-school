# Задание: "Словарь 3_1"

from string import ascii_lowercase


alphabet = {}


for num, letter in enumerate(list(ascii_lowercase)):
    alphabet[letter] = num + 1


for value in alphabet:
    print(f"{value}: {alphabet[value]}")
