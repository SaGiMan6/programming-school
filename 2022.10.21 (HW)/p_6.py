with open("prices.txt", mode="r", encoding="utf-8") as file:
    a = file.read().split("\n")


s = 0


for num, val in enumerate(a):
    vt = val.split("\t")
    v1 = int(vt[1])
    v2 = int(vt[2])
    s += v1 * v2
    print(s)


print(s)
