a = set(list(map(int, input().split())))

l_a = list(a)

s = 0


for i in range(len(l_a)):
    s += l_a[i] ** 2

a.add(s)


print(a)
