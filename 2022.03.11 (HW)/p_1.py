a = input()

x = a.find("f")
y = a.rfind("f")

if x > -1:
    if x == y:
        print(x)
    else:
        print(x, y)
else:
    print("NO")
