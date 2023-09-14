def swap_columns(a, i, j):
    l = len(a)

    for k in range(l):
        a[k][i], a[k][j] = a[k][j], a[k][i]

    for k in range(l):
        print(*a[k])


n, m = map(int, input().split())

a = [[] for i in range(n)]


for i in range(n):
    a[i] = list(map(int, input().split()))


i, j = map(int, input().split())


swap_columns(a, i, j)
