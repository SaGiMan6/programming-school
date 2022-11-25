print("Массив:")

a = input().split()


mx = max(a)
cou = 0


for num, chis in enumerate(a):
    if chis == mx:
        cou += 1


print(f"Максимальное значение: {mx}")
print(f"Количество элементов: {cou}")