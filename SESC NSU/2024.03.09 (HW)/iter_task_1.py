# Грехов Александр 11-10

import itertools


def find_word(k, m, n):
    letters = list(map(chr, range(65, 65 + m)))
    combinations = list(itertools.product(letters, repeat=n))
    result = ''.join(combinations[k - 1])
    return result


K = int(input())
M = int(input())
N = int(input())

print(find_word(K, M, N))