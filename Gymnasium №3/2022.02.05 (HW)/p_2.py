print(2)


a = input()
b = ""

for i in range(len(a)):
    if a[i] == "1":
        b = b + "0"
    if a[i] == "0":
        b = b + "1"
    if a[i] != "1" and a[i] != "0":
        b = b + a[i]

print(b)