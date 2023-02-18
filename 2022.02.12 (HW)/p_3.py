print(3)


print("Введите адрес файла")

a = input()

b = a.split("/")

for i in range(len(b)):
    print(b[i])
