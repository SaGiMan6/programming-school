with open("numbers.txt", mode="r", encoding="utf-8") as file:
    text = file.read().split("\n")


for num, line in enumerate(text):
    sm = 0

    ln = line.split(" ")

    for n, zn in enumerate(ln):
        if str(zn) != "":
            sm += int(zn)

    if sm != 0:
        print(sm)
