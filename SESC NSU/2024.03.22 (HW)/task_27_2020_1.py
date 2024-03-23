# Грехов Александр 11-10

def findPairWithMaxSum(arr, n):
    max_element = max(arr[0], arr[1])
    second_max_element = min(arr[0], arr[1])

    for i in range(2, n):
        if arr[i] > max_element:
            second_max_element = max_element
            max_element = arr[i]
        elif arr[i] > second_max_element:
            second_max_element = arr[i]

    return (max_element, second_max_element)


arr = [3, 1, 5, 2, 4]
n = len(arr)

result = findPairWithMaxSum(arr, n)

print(result)
