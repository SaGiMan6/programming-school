# Грехов Александр 11-10

def combinations(alphabet, n, prefix=""):
    if n == 0:
        print(prefix)
    else:
        for i in range(len(alphabet)):
            combinations(alphabet[i+1:], n-1, prefix + alphabet[i])

# Запуск функции с M=3 и N=2
combinations("ABC", 2)
