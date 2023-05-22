# Задание: "Словарь 3_1"

n = int(input())

nums = {}


for value in range(1, n + 1):
    nums[value] = value ** 2


for value in nums:
    print(f"{value}: {nums[value]}")
