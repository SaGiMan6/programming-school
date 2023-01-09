from random import randint, choice


def sortv(ms):
    if len(ms) <= 1:
        return ms
    x = choice(ms)
    b1 = [b for b in ms if b < x]
    bx = [b for b in ms if b == x]
    b2 = [b for b in ms if b > x]
    return sortv(b1) + bx + sortv(b2)

def sortu(ms):
    if len(ms) <= 1:
        return ms
    x = choice(ms)
    b1 = [b for b in ms if b > x]
    bx = [b for b in ms if b == x]
    b2 = [b for b in ms if b < x]
    return sortu(b1) + bx + sortu(b2)


print("Введите длинну массива:")
n = int(input())
if n > 2 and (n % 2) == 0:
    a = [randint(1, 9) for i in range(n)]
else:
    print("Введена некоректная длинна массива")
    print("Выбранна стандартная длинна - 8")
    n = 8
    a = [randint(1, 9) for i in range(n)]


print("Массив:")
print(*a)

print("После сортировки:")
print(*(sortv(a[:n // 2]) + sortu(a[n // 2:])))
