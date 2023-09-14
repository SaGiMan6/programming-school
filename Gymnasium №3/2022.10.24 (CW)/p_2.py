from random import randint


s = []

for i in range(25):
    s += str(randint(111, 777)) + "\n"


with open("random.txt", mode="w", encoding="utf-8") as file:
    file.writelines(s)
