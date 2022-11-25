a, b, c = map(int, input("Введите рост спортсменов").split())


if a == min(a, b, c) and c == max(a, b, c):
    print("По росту")
else:
    print("Не по росту")
