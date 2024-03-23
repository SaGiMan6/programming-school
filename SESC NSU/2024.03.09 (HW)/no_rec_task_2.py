# Грехов Александр 11-10

from math import factorial


def get_permutation(n, m, k):
    alphabet = [chr(i) for i in range(65, 65 + m)]
    total_permutations = factorial(m) // factorial(m - n)

    k = k % total_permutations if k > total_permutations else k

    def get_kth_permutation(sequence, k):
        permutation = []
        while sequence:
            total_permutations = factorial(len(sequence) - 1)
            index, k = divmod(k, total_permutations)
            permutation.append(sequence.pop(index))
        return permutation

    kth_permutation = get_kth_permutation(alphabet, k - 1)
    return ''.join(kth_permutation[:n])


k = 4
m = 3
n = 2

print(get_permutation(n, m, k))
