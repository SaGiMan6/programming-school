a = set(list(map(int, list(str(input())))))
b = set(list(map(int, list(str(input())))))


if (a & b) == set():
    print("NO")
else:
    print("YES")
