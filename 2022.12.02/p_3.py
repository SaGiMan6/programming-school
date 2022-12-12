from random import randint


p = 50
n = 1000
sm_sch_pz = 0
sm_sch_v = 0


for i in range(p):
    a = [0 for i in range(n)]

    for i in range(n):
        a[i] = randint(1, 10000)

    b = a


    sch_pz = 0
    sch_v = 0


    for i in range(n - 1):
        for j in range(n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                sch_pz += 1

    for i in range(0, n - 1):
        smallest = i
        for j in range(i + 1, n):
            if b[j] < b[smallest]:
                smallest = j
        b[i], b[smallest] = b[smallest], b[i]
        sch_v += 1

    sm_sch_pz += sch_pz
    sm_sch_v += sch_v


print("Массивы были отсортированы 50 раз, двумя методами")
print(f"В среднем для сортировки 1000 элементов пузырьком перестановка происходила {sm_sch_pz // 50}")
print(f"В среднем для сортировки 1000 элементов выбором перестановка происходила {sm_sch_v // 50}")
