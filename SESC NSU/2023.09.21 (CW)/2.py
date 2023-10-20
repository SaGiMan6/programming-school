print("x y z w")

for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                """ if (x or not(y)) and (not(y == z)) and not(w):
                    print(x, y, z, w )"""
                if ((y <= x) == (x <= w)) and (z or x):
                    print(x, y, z, w)