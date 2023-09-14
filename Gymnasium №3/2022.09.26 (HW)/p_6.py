a = str(input("Введите последовательность чисел \n"))
b = []
c = 0


for num, ch in enumerate(a):
    b.append(int(ch))

for num, ch in enumerate(b):
    if b.count(ch) == 2:
        c = 2


if c == 2:
    print("Да")
else:
    print("Нет")
