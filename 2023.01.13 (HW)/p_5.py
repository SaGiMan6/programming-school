n = int(input())

m = [[0 for j in range(n)] for i in range(n)]


for i in range(n):
    for j in range(n):
        if (i + j) == (n - 1):
            m[i][j] = 1
        elif (i + j) > (n - 1):
            m[i][j] = 2


for i in range(n):
    print(*m[i])
