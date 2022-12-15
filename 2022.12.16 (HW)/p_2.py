from random import randint


print("Введите размер квадратной матрицы:")
r = int(input())


m = []
s = 0
sr = 0


for i in range(r):
    m.append(list())
    for j in range(r):
        m[i].append(randint(10, 99))


print("\nМатрица А:")
for i in m:
    print(*i)


for i in range(r):
    s += m[i][i]
    sr += m[r - 1 - i][i]


print("\nСумма элементов главной диагонали:")
print(s)

print("\nСреднее арифметическое побочной диагонали:")
print(sr / r)
