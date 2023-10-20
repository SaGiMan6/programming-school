def xor(a, b):
    return bool(a) != bool(b)


print("x z  F")

for x in range(2):
    for z in range(2):
        print(x, z, end="  ")
        if xor(x, not z):
            print(1)
        else:
            print(0)
