n = int(input())

m = [[0 for j in range(n)] for i in range(n)]


for i in range(n):
    for j in range(n):
        m[i][j] = abs(i - j)


for i in range(n):
    print(*m[i])
