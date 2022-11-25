from random import randint


a = []


for i in range(randint(3, 15)):
    a.append(randint(-100, 100))


mx1 = max(a)
mx1i = a.index(mx1)
mx2 = -101
mx2i = -1


for num, chis in enumerate(a):
    if chis > mx2 and num != mx1i:
        mx2 = chis
        mx2i = num


print("Массив:")
for num, chis in enumerate(a):
    print(chis, end=" ")
    if num + 1 == len(a):
        print()
print(f"Максимальный элемент: A[{mx1i+1}] = {mx1}")
print(f"Второй максимальный элемент: A[{mx2i+1}] = {mx2}")