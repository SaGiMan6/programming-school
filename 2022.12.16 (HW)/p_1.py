print("Введите количество строк матрицы:")
rv = int(input())

print("\nВведите количество столбцов матрицы:")
rsh = int(input())


m = []


for i in range(rv):
    m.append(list())
    for j in range(rsh):
        m[i].append(f"{i}{j}")


print("\nПолученная матрица:")
for i in m:
    print(*i)
