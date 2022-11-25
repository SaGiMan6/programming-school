with open("numbers.txt", mode="r", encoding="utf-8") as file:
    a = file.read().split("\n")

s = int(a[0]) + int(a[1])


print(s)
