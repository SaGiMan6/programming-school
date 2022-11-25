new_text = ""


with open("text.txt", mode="r", encoding="utf-8") as file:
    text = file.read()


for num, lit in enumerate(text):
    new_text += text[((num + 1) * -1)]


print(new_text)
