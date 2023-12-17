# Найти на интервале [n, m] числа, которые имеют ровно 3 различных делителя, отличных от 1 и самого числа.
# Числа n и m вводятся с клавиатуры и могут быть велики.

from math import floor, ceil


def brh(x, y):
    m = [i for i in range(y + 1)]
    m[0] = 1

    for i in range(2, y + 1):
        if m[i] != 1:
            j = 2 * i
            while j <= y:
                m[j] = 1
                j += i
    return [r for r in m if r != 1 and r >= x]


n = int(input())
m = int(input())

up_border = floor(m ** 0.25)
down_border = ceil(n ** 0.25)

result = brh(down_border, up_border)
for i in result:
    print(f"{i}^4")
