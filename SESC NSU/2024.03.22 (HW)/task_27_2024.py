# Грехов Александр 11-10

def maxSumWithMinDistance(arr, n, k):
    if n < 3:
        return 0
    max_sum = float('-inf')
    for i in range(n - 2):
        for j in range(i + k, n - 1):
            for m in range(j + k, n):
                current_sum = arr[i] + arr[j] + arr[m]
                max_sum = max(max_sum, current_sum)

    return max_sum


with open('file.txt', 'r') as file:
    k = int(file.readline())
    n = int(file.readline())
    arr = [int(file.readline()) for _ in range(n)]

result = maxSumWithMinDistance(arr, n, k)

print(result)
