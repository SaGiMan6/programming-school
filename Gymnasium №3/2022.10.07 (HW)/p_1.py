for i in range(-150, 450):
    s = 0

    if i > 0:
        for j in range(1, 450):
            if i % j == 0:
                s += 1

    if i < 0:
        for j in range(1, 150):
            if abs(i) % abs(j) == 0:
                s += 1

    if s == 5:
        print(i)
