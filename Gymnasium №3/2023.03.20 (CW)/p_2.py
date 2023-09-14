a = set(list(map(int, list(str(input())))))
b = set(list(map(int, list(str(input())))))


if (b - a) == set():
    print("YES")
else:
    print("NO")
