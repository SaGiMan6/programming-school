from random import randint


print("Введите размер квадратной матрицы")
r = int(input())


mn = 100
mx = 0

ind_mn = "[0, 0]"
ind_mx = "[0, 0]"

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
        if m[i][j] < mn:
            mn = m[i][j]
            ind_mn = f"[{i + 1}, {j + 1}]"
        if m[i][j] > mx:
            mx = m[i][j]
            ind_mx = f"[{i + 1}, {j + 1}]"


print("Максимальный элемент А" + ind_mx + f" = {mx}")
print("Минимальный элемент А" + ind_mn + f" = {mn}")
