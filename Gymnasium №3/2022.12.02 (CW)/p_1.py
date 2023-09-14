from random import randint


n = randint(1, 8) * 2

a = [0 for i in range(n)]

for i in range(n):
    a[i] = randint(1, 30)


print("Массив:")
for i in range(n):
    print(a[i], end=" ")
print()


a[:(n // 2)] = sorted(a[:(n // 2)])
a[(n // 2):] = sorted(a[(n // 2):], reverse=True)


print("Массив после сортировки:")
for i in range(n):
    print(a[i], end=" ")
print()
