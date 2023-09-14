# with open("27A.txt", mode="r") as file:
#     read_file = file.read().split("\n")
#
# n, k, m = map(int, read_file[0].split())
# data = list(map(int, read_file[1:]))
#
# for num, case in enumerate(data):
#     data[num] = case % 100
#
# amount = 0
#
# for i in range(k, n):
#
#
#
#
from tqdm import tqdm

#Помещение данных из файла в переменные
with open("27B.txt", mode="r") as file:
    s = file.read()
    n, k, m = map(int, s.split("\n")[0].split(" "))
    r = list(map(int, s.split("\n")[1:-1]))

#Замена чисел их остатками при делении на сто
r = [i % 100 for i in r]

c = 0
for i in tqdm(range(k, m + 1)):
    s = sum([r[i] for i in range(0, i)]) % 100
    if s == 24:
        c += 1
    for j in range(i, n):
        s = (s - r[j - i] + r[j]) % 100
        if s == 24:
            c += 1
print(c)