print(1)


a = input()
b = ""

for i in range(len(a)):
    if a[i] == ".":
        b = b + "0"
    if a[i] == "X":
        b = b + "1"

print(b)