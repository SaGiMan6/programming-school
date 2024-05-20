# Решение 25 задачи ЕГЭ с помощью fnmatch (3)

import fnmatch
import math


def is_power_of_two(n):
    return (n != 0) and (n & (n - 1) == 0)


def count_divisors(n):
    count = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            if n / i == i:
                count = count + 1
            else:
                count = count + 2
    return count


max_num = 10**9 // 2031

for i in range(1, max_num + 1):
    if fnmatch.fnmatch(str(i * 2031), "*31*65") and is_power_of_two(count_divisors(i * 2031)) and (i * 2031) % 31 == 0:
        print(i * 2031)
