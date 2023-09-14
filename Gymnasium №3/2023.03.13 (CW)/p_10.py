n, m = map(int, input().split())

a = set()
b = set()


for i in range(n):
    a.add(int(input()))

for i in range(m):
    b.add(int(input()))


print("Количество цветов в обоих наборах:", len(a & b))
print("Цвета в обоих наборах:")
print(a & b, "\n")

print("Количество цветов, которые есть только у Ани:", len(a - b))
print("Цвета, которые есть только у Ани:")
print(a - b, "\n")

print("Количество цветов, которые есть только у Бори:", len(b - a))
print("Цвета, которые есть только у Бори:")
print(b - a, "\n")
