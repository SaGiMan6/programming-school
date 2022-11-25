for i in range(1, 6):

    for j in range(i):
        if j == i - 1:
            print(3, end=" ")
        else:
            print(2, end=" ")

    print()

    for j in range(i):
        if j == i - 1:
            print(0, end=" ")
        else:
            print(j - i + 11, end=" ")

    print()
