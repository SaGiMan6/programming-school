import string, itertools

alphabet = string.ascii_uppercase

k = int(input("Введите порядковый номер слова: "))
m = int(input("Введите количество букв в алфавите: "))
n = int(input("Введите длину искомого слова: "))

result_words = itertools.combinations_with_replacement(alphabet[:m], n)
for i in range(k):
    word = next(result_words)
    print(*word)


print(f"Слово {k}-е в словарном порядке: {word}")
