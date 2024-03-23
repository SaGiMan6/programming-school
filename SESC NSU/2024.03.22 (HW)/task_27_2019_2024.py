# Грехов Александр 11-10

def countPairsDivisibleBy29(arr, n):
    count = 0

    for i in range(n - 4):
        for j in range(i + 4, n):
            if arr[i] * arr[j] % 29 == 0:
                count += 1

    return count


n = int(input())
arr = [int(input()) for _ in range(n)]

result = countPairsDivisibleBy29(arr, n)

print(result)
