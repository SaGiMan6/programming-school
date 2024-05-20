# Грехов Александр 11-10

def combinations(alphabet, n, prefix=""):
    if n == 0:
        print(prefix)
    else:
        for i in range(len(alphabet)):
            combinations(alphabet[i+1:], n-1, prefix + alphabet[i])

N = 2
M = 3
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

combinations(alphabet[:M], N)
