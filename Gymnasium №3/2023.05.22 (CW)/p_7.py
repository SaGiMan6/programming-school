# Задание: "Словарь 4"

words = ['hello', 'bye', 'yes', 'no', 'python', 'apple', 'maybe', 'stepik', 'beegeek']


result = {word: [ord(word[letter]) for letter in range(len(word))] for word in words}


for key in result:
    print(f"{key}: {result[key]}")
