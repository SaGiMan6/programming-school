print("Введите количество строк матрицы")
rv = int(input())

print("Введите количество столбцов матрицы")
rsh = int(input())


m = [[0 for i in range(rsh)] for j in range(rv)]

sch = 0


for i in range(rsh):
    for j in range(rv):
        sch += 1
        if i % 2 == 0:
            m[j][i] = sch
        else:
            m[(-1 * (j + 1))][i] = sch


print("Результат:", end="")
for i in range(rv):
    print()
    for j in range(rsh):
        print(m[i][j], end=" ")
