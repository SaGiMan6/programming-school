a = set(list(map(int, input().split())))
b = set(list(map(int, input().split())))
c = set(list(map(int, input().split())))


print(*reversed(sorted((c - b) - a)))
