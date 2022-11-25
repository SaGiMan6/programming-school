with open("input.txt", mode="r", encoding="utf-8") as file:
    a = file.read().split("\n")


for num, val in enumerate(a):
    a[num] = str(num + 1) + ") " + a[num] + "\n"


with open("output_2.txt", mode="w", encoding="utf-8") as file:
    file.writelines(a)
