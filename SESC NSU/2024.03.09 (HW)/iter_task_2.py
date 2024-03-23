# Грехов Александр 11-10

from itertools import permutations


def kth_permutation(k, m, n):
    letters = [chr(65 + i) for i in range(m)]
    perms = list(permutations(letters, n))
    kth_perm = perms[(k - 1) % len(perms)]
    print(''.join(kth_perm))


K, M, N = map(int, input().split())
kth_permutation(K, M, N)
