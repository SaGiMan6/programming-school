# Задание №1 (23)
# Исполнитель умеет выполнять 2 действия:
# 1 - прибавлять 1
# 2 - умножать число на 2
#
# Сколькими способами исполнитель может получить 25 из 3

def path_counter(x, y):
    if x < y:
        return path_counter(x + 1, y) + path_counter(x * 2, y)
    elif x == y:
        return 1
    else:
        return 0


print(path_counter(3, 25))
