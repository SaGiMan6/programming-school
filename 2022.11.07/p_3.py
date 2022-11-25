m = 0


with open("lines.txt", mode="r", encoding="utf-8") as file:
    text = file.read().split("\n")


for num, line in enumerate(text):
    if len(line) > m:
        m = len(line)


for num, line in enumerate(text):
    if len(line) == m:
        print(line)
