from random import randint


print("Введите количество строк матрицы")
rv = int(input())

print("Введите количество столбцов матрицы")
rsh = int(input())


m = []


for i in range(rv):
    m.append(list())
    for j in range(rsh):
        m[i].append(randint(0, 255))


print("Матрица А:", end="")
for i in range(rv):
    print()
    for j in range(rsh):
        print(m[i][j], end=" ")
print()


for i in range(rv // 2):
    m[i], m[(-1 * (i + 1))] = m[(-1 * (i + 1))], m[i]


print("Результат:", end="")
for i in range(rv):
    print()
    for j in range(rsh):
        print(m[i][j], end=" ")
