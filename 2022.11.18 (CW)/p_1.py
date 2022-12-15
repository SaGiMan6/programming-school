from random import randint


a = []


for i in range(randint(3, 15)):
    a.append(randint(-100, 100))


mx = max(a)
mxn = a.index(mx)

mn = min(a)
mnn = a.index(mn)


print("Массив:")
for num, chis in enumerate(a):
    print(chis, end=" ")
    if num + 1 == len(a):
        print()
print(f"Максимальный элемент: A[{mxn+1}] = {mx}")
print(f"Максимальный элемент: A[{mnn+1}] = {mn}")