from random import randint


a = []
b = []


for i in range(randint(3, 15)):
    a.append(randint(0, 100))


for num, chis in enumerate(a):
    sch = 0

    for i in range(chis, 1, -1):
        if chis % i == 0:
            sch += 1

    if sch < 2 and chis != 0:
        b.append(chis)


print("Массив A:")
for num, chis in enumerate(a):
    print(chis, end=" ")
    if num + 1 == len(a):
        print()
print("Массив B:")
for num, chis in enumerate(b):
    print(chis, end=" ")
    if num + 1 == len(b):
        print()