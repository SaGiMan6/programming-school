# Грехов Александр 11-10

def find_arrangement(k, m, n):
    def generate_arrangements(arr, num, result):
        if num == 0:
            result.append(''.join(arr))
            return

        for i in range(m):
            if not arr or arr[-1] != chr(65+i):
                arr.append(chr(65+i))
                generate_arrangements(arr, num - 1, result)
                arr.pop()

    arrangements = []
    generate_arrangements([], n, arrangements)
    result = arrangements[(k - 1) % len(arrangements)]

    return result


K = 4
M = 3
N = 2

print(find_arrangement(K, M, N))