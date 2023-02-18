a = input()
if a[0] == a[-1]:
    print("Yes")
else:
    print("No")


b = ""
for i in a:
    if i == "и":
        b += "и"
print(b)


c = 0
for i in a:
    if i == "о":
        c += 1
print(b)


d = ""
for i in a:
    if i == " ":
        c += "_"
    else:
        c += i
print(b)


