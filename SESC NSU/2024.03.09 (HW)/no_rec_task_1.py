# Грехов Александр 11-10

def find_arrangement(k, m, n):
    arrangements = []
    stack = []
    stack.append(([], n))
    while stack:
        arr, n = stack.pop()
        if n == 0:
            arrangements.append(''.join(arr))
        else:
            for i in range(m):
                if not arr or arr[-1] != chr(65+i):
                    new_arr = arr + [chr(65+i)]
                    stack.append((new_arr, n-1))
    result = arrangements[(k - 1) % len(arrangements)]
    return result


K = 4
M = 3
N = 2

print(find_arrangement(K, M, N))
