def prost(x):
    y = x
    z = 0
    while x > 1:
        if y % x == 0:
            z += 1
        x -= 1
    return z


n = int(input())


for i in range(2, n + 1):
    if prost(i) == 1:
        print(i, end=" ")
