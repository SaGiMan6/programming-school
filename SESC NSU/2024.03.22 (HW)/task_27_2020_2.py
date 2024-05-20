# Грехов Александр 11-10

def countPairsWithDivisibleSum(arr, n, m):
    divisibleCount = 0
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] > arr[j]:
                if (arr[i] + arr[j]) % m == 0:
                    divisibleCount += 1
    return divisibleCount


arr = [1, 3, 113, 112, 5, 2, 4, 117, 4, 7, 3]
n = len(arr)

result = countPairsWithDivisibleSum(arr, n, 120)

print(result)
