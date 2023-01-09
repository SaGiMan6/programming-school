from random import randint, choice


def sortv(ms):
    if len(ms) <= 1:
        return ms
    x = choice(ms)
    b1 = [b for b in ms if b < x]
    bx = [b for b in ms if b == x]
    b2 = [b for b in ms if b > x]
    return sortv(b1) + bx + sortv(b2)


print("Введите длинну массива:")
n = int(input())

a = [randint(1, 9) for i in range(n)]


print("Массив:")
print(*a)


b = sortv(a)

print("После сортировки:")
print(*b)
print(f"Различных чисел: {len(set(b))}")
