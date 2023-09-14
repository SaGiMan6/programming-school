from random import randint


print("Введите размер квадратной матрицы")
r = int(input())


m = []


for i in range(r):
    m.append(list())
    for j in range(r):
        m[i].append(randint(10, 99))


print("Матрица А:", end="")
for i in range(r):
    print()
    for j in range(r):
        print(m[i][j], end=" ")
print()


for i in range(r):
    for j in range(r):
        if j > i:
            m[i][j] = 0


print("Результат:", end="")
for i in range(r):
    print()
    for j in range(r):
        print(m[i][j], end=" ")
