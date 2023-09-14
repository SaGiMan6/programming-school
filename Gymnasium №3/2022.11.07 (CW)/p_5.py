chsl = "0123456789"
new_text = ""
sm = 0


with open("nums.txt", mode="r", encoding="utf-8") as file:
    text = file.read().replace("\n", " ")


for num, lit in enumerate(text):
    if lit in chsl:
        new_text += lit
    else:
        new_text += " "


newer_text = new_text.split(" ")


for num, lit in enumerate(newer_text):
    if str(lit) != "":
        sm += int(lit)


print(sm)
