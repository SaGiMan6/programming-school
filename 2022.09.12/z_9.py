a = 100


while a < 1000:
    if a == (((a // 100) ** 3) + (((a % 100) // 10) ** 3) + ((a % 10) ** 3)):
        print(a, end=" ")
    a += 1
