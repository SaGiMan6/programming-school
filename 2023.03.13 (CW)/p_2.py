a = set(list(map(int, input().split())))
b = set(list(map(int, input().split())))


a.difference_update(b)


print(a)
