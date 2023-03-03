ch = list(map(int, input().split()))

mn = set()
otv = []


for i in range(len(ch)):
    if ch[i] in mn:
        otv.append("YES")
    else:
        otv.append("NO")
        mn.add(ch[i])


print(*otv)