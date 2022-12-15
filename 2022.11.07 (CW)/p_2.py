with open("data.txt", mode="r", encoding="utf-8") as file:
    text = file.read().split("\n")


for i in range(-1, (len(text) + 1) * -1, -1):
    print(text[i])