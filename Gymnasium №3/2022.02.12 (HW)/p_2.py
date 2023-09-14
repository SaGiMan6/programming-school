print(2)


print("Введите фамилию, имя и отчество")

a = input()

b = a.split()
a = b[1]
c = b[2]

print(a[0] + "." + c[0] + ". " + b[0])
