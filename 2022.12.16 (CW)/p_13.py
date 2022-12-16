from random import randint


r = 6

m = []


for i in range(r):
    m.append(list())
    for j in range(r):
        m[i].append(randint(-100, 200))


print("Матрица А:")
for i in m:
    print(*i)

print("\n" + "Элементы главной диагонали")
for i in range(r):
    print(m[i][i], end=" ")

print("\n" + "\n" + "Элементы побочной диагонали")
for i in range(r):
    print(m[r - 1 - i][i], end=" ")
