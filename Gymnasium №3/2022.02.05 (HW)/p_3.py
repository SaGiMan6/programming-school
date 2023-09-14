print(1)


a = input()
b = ""

for i in range(len(a)):
    if a[i] == "1":
        b += 1

if b % 2 == 0:
    a = a + "0"
else:
    a = a + "1"

print(a)