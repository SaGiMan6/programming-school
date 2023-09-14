n = int(input())

gls = dict()

cnds = dict()


for _ in range(n):
    gl = input().split()
    gls[gl[0]] = gl[1]


for gl in gls:
    if gl in cnds:
        cnds[gl] += gls[gl]
    else:
        cnds[gl] = gls[gl]


for cnd in sorted(cnds):
    print(f"{cnd} {cnds[cnd]}")
