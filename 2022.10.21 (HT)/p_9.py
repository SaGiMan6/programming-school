with open("lines.txt", mode="r", encoding="utf-8") as file:
    a = file.read().split("\n")


max_len = 0


for num, val in enumerate(a):
    if len(val) > max_len:
        max_len = len(val)

for num, val in enumerate(a):
    if len(val) == max_len:
        print(val)
