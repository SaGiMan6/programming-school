a = 8
b = 30
c = int(input("Введите номер урока"))

b = b + (c * 55) - 10
a = a + (b // 60)
b = b % 60


print(a, b)
