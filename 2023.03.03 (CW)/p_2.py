mn_1 = set(list(map(int, input().split())))
mn_2 = set(list(map(int, input().split())))


print(*(sorted(mn_1 & mn_2)))