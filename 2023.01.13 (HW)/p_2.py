n = int(input())

m = [["." for j in range(n)] for i in range(n)]


for i in range(n):
    for j in range(n):
        if j == i or (i + j) == (n - 1) or j == ((n - 1) // 2) or i == ((n - 1) // 2):
            m[i][j] = "*"


for i in range(n):
    print(*m[i])
