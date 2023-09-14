# В этом файле написаны обе программы


# Программа №1

fb = "ФТК1\nФТК2\nФТК3\nФТК4\nФТК5\nФТК6\nФТК7\nФТК8\nФТК9\nФТК10\nФТК11\nФТК12\nФТК13\nФТК14\nФТК15"
# Я не знаю названий футбольных клубов, поэтому они условно будет озозначаться как ФТК (ФуТбольный Клуб)


with open("football.txt", mode="w") as file_1:
    file_1.writelines(fb)


# Программа №2

with open("football.txt", mode="r") as file_2:
    rd = file_2.read().split("\n")


for num, com in enumerate(rd):
    print(str(num + 1) + ". " + com)
