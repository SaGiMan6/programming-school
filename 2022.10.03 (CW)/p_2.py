a = 185

for x in range(14):
    for y in range(11):
        for z in range(9):
            if (15 * x) + (17 * y) + (21 * z) == 185:
                print(x, " ящиков по 15 кг\n", end="")
                print(y, " ящиков по 17 кг\n", end="")
                print(z, "ящиков по 21 кг\n")
