def mlt(x, y):
    s = 0

    for i in range(y):
        s += x

    return s


a = int(input("Введите первое число\n"))
b = int(input("Введите второе число\n"))


if a > 0 and b > 0:
    print(mlt(a, b))
elif (a > 0 and b < 0) or (a < 0 and b > 0):
    print(mlt(abs(a), abs(b)) * -1)
elif a < 0 and b < 0:
    print(mlt(abs(a), abs(b)))
elif a == 0 or b ==0:
    print(0)