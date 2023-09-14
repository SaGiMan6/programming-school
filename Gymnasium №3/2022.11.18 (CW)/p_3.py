from random import randint


a = []
b = []


for i in range(randint(3, 15)):
    a.append(randint(-10, 10))


for num, chis in enumerate(a):
    if chis % 2 == 0 and chis < 0:
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