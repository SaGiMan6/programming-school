n, m = map(int, input().split())

a = [["." for j in range(m)] for i in range(n)]


for i in range(n):
    for j in range(m):
        if ((i + j) % 2) != 0:
            a[i][j] = "*"


for i in range(n):
    print(*a[i])
