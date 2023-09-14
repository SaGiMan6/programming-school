a, b = map(int, input("Стоимость пирожка").split())
c = int(input("Сколько пирожков"))


a = a * c
b = b * c
a = a + (b // 100)
b = b % 100


print("К оплате:", a, "Руб.", b, "Коп.")
