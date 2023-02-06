n, m = map(int, input().split())

a = [[] for j in range(n)]

for i in range(n):
    a[i] = list(map(int, input().split()))


mxc = a[0][0]
mxi = [0, 0]


for i in range(n):
    for j in range(m):
        if a[i][j] > mxc:
            mxc = a[i][j]
            mxi = [i, j]


print(str(mxi[0]) + " " + str(mxi[1]))
