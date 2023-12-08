# Задание №2 (23)
# Исполнитель умеет выполнять 3 элементарных действия:
# 1 - вычитать 1,
# 2 - вычитать 2,
# 3 - вычитать 3.
#
# Посчитать количество программ, которые превращают 50 в 5 и проходят через промежуточные значения 40 и 20.
# Через оба!

def path_counter(x, y):
    if x > y:
        return path_counter(x - 1, y) + path_counter(x - 2, y) + path_counter(x - 3, y)
    elif x == y:
        return 1
    else:
        return 0


print(path_counter(50, 40) * path_counter(40, 20) * path_counter(20, 5))
