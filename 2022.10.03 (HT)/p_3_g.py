a = 0
a1 = 0
b = 1
c = 0

for i in range(5, 0, -1):

    for j in range(i):

        if a == 0:
            print(5, end=" ")
        elif a == 1:
            print(b, end=" ")
        elif a == 2:
            print(0, end=" ")
        elif a == 3:
            print(b, end=" ")

    a += 1
    a1 += 1

    if a == 1 or a == 3:
        c += 1
    if a > 3:
        a = 0
    if c > 1:
        c = 0
        b += 1

    if a1 > 1:

        print()

        for j in range(i):

            if a == 0:
                print(5, end=" ")
            elif a == 1:
                print(b, end=" ")
            elif a == 2:
                print(0, end=" ")
            elif a == 3:
                print(b, end=" ")

        a += 1
        a1 += 1

        if a == 1 or a == 3:
            c += 1
        if a > 3:
            a = 0

    print()
