with open("nums.txt", mode="r", encoding="utf-8") as file:
    a = file.read().split("\n")

for num, el in enumerate(a):
    a[num] = a[num].replace(" ", "")

for num, el in enumerate(a):
    if el == "":
        a.pop(num)

print(a)