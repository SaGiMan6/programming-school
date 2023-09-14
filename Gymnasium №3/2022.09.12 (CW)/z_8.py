a = 10000


while a < 100000:
    if a % 133 == 125 and a % 134 == 111:
        print(a, end=" ")
    a += 1
