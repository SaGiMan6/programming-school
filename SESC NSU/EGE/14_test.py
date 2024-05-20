alp = "0123456789abcdefgh"
for x in alp:
    a = int("9009" + x, 18)
    b = int("2257" + x, 18)
    if (a + b) % 15 == 0:
        print((a + b) // 15)
