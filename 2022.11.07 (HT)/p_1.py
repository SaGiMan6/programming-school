eng_ltrs = "etaoinshrdlcumwfgypbvkxjqz"
num_ltrs = 0
num_wrds = 0


with open("file.txt", mode="r", encoding="utf-8") as file:
    txt = file.read()


ltrs = txt.replace("\n", " ").lower()
for num, ltr in enumerate(ltrs):
    if ltr in eng_ltrs:
        num_ltrs += 1


txt = txt.split("\n")
num_lns = len(txt)


for num, line in enumerate(txt):
    txt[num] = line.split(" ")
    num_wrds += len(txt[num])


print("Input file contains:")
print(num_ltrs, "letters")
print(num_wrds, "words")
print(num_lns, "lines")
