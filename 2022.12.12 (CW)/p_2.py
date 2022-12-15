from random import randint


print("Введите количество строк матрицы")
rv = int(input())

print("Введите количество столбцов матрицы")
rsh = int(input())


sm = 0

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


for i in range(rv):
    for j in range(rsh):
        sm += m[i][j]

sr = sm / (rv * rsh)
print(f"Средняя яркость {sr}")


for i in range(rv):
    for j in range(rsh):
        if m[i][j] < sr:
            m[i][j] = " 0 "
        else:
            m[i][j] = "255"


print("Результат:", end="")
for i in range(rv):
    print()
    for j in range(rsh):
        print(m[i][j], end=" ")
