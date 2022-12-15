from random import randint


n = randint(2, 12)

a = [0 for i in range(n)]

for i in range(n):
    a[i] = randint(1, 8)


print("Массив:")
for i in range(n):
    print(a[i], end=" ")
print()


a = sorted(a)
r = len(set(a))


print("Массив после сортировки:")
for i in range(n):
    print(a[i], end=" ")
print(f"\nРазличных чисел: {r}")
