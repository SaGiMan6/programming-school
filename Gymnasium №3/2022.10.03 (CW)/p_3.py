n = int(input(""))


for i in range(1, n + 1):

    c = list(str(i))
    s = 0

    try:
        for num, chi in enumerate(c):
            if i % int(chi) != 0:
                s += 1

    except ZeroDivisionError:
        s += 1

    if s == 0:
        print(i, end=" ")