def prst(x, y):

    s = 0

    for j in range(1, (y // 2) + 2):
        if x % j == 0:
            s += 1

    if s < 2:
        print(x)


a = int(input())
b = int(input())


for i in range(a, b):
    prst(i, b)
