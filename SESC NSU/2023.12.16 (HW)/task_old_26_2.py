# Мардж и Гаммер Симпсоны обзавелись пропуском на все голливудские приёмы на ноябрь.
# У них есть список приёмов, в котором обозначены время начала и конца всех приёмов.
#
# Гоммер хочет посетить максимальное количество приёмов, поскольку на каждом из них можно наесться.
# При прочих равных условиях, Мардж хочет вернуться как можно раньше, поскольку дети дома одни (с дедушкой).

print("Вводите пары начала и конца приема (в секундах/минутах от начала ноября) через пробел")
print("После последней пары введите 0")

receptions = []
ipt = input()
while ipt != "0":
    receptions.append(list(map(int, ipt.split())))
    ipt = input()

receptions.sort(key=lambda x: x[1])

k_receptions = [receptions[0]]
receptions.pop(0)
for reception in receptions:
    if k_receptions[-1][1] <= reception[0]:
        k_receptions.append(reception)

print(f"Максимальное количество приемов - {len(k_receptions)}")
