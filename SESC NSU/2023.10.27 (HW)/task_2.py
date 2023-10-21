# Задание 2

# Имеется набор данных, состоящий из пар положительных целых чисел.
# Необходимо выбрать из каждой пары ровно одно число так,
# Чтобы сумма всех выбранных чисел делилась на 3 и при этом была минимально возможной.
# Если получить требуемую сумму невозможно, в качестве ответа нужно выдать 0.


from random import randint


data = []

# Генерируем количество чисел, указанное пользователем
n = int(input("How many pairs you want to check? ").strip())
for i in range(n):
    data.append([randint(1, 100), randint(1, 100)])


min_in_pair_sum = 0

# Делаем так, чтобы первым в паре было минимальное число пары, вторым - максимальное
for number, pair in enumerate(data):
    min_in_pair = min(pair[0], pair[1])
    max_in_pair = max(pair[0], pair[1])
    data[number] = [min_in_pair, max_in_pair]

    min_in_pair_sum += min_in_pair


# 1. Проверяем, делится ли сумма первых чисел пар на 3, если делится, выводим сумму

# 2. Если сумма делится на 3 с остатком 1.

# 2.1. Ищем пару с минимальной разницей чисел,
# Где в паре разница остатков от деления на 3 большего числа и меньшего числа равна 3
# Из такой пары мы берем большее число и тогда сумма меняется наименьшим образом и делится на 3

# 2.2 Ищем две пары с минимальной разницей чисел,
# Где в каждой паре разница остатков от деления на 3 большего числа и меньшего числа равна 1

# 2.3 Проверяем, где меньше меняется сумма, если менять две пары или одну,
# Меняем так, чтобы изменения изначально суммы были минимальны

# 2.4 Если не получилось найти пары, выводим 0,
# Так как невозможно получить сумму, делящуюся на 3

# 3. Если сумма делится на 3 с остатком 2.

# 3.1. Ищем пару с минимальной разницей чисел,
# Где в паре разница остатков от деления на 3 большего числа и меньшего числа равна 1
# Из такой пары мы берем большее число и тогда сумма меняется наименьшим образом и делится на 3

# 3.2 Ищем две пары с минимальной разницей чисел,
# Где в каждой паре разница остатков от деления на 3 большего числа и меньшего числа равна 2

# 3.3 Проверяем, где меньше меняется сумма, если менять две пары или одну,
# Меняем так, чтобы изменения изначально суммы были минимальны

# 3.4 Если не получилось найти пары, выводим 0,
# Так как невозможно получить сумму, делящуюся на 3

if min_in_pair_sum % 3 == 0:
    print(f"Max sum is {min_in_pair_sum}")

elif min_in_pair_sum % 3 == 1:
    perfect_pair = -1
    pair_min_difference = 1000

    for number, pair in enumerate(data):
        if (pair[1] % 3) - (pair[0] % 3) == 2:
            if pair_min_difference > (pair[1] - pair[0]):
                perfect_min_difference = pair[1] - pair[0]
                perfect_pair = number

    perfect_pairs = [-1, -1]
    pairs_min_difference = [1000, 1000]

    for number, pair in enumerate(data):
        if (pair[1] % 3) - (pair[0] % 3) == 1:
            if pairs_min_difference[1] > (pair[1] - pair[0]):
                perfect_min_difference = pair[1] - pair[0]
                perfect_pairs[1] = number
        if pairs_min_difference[0] > pairs_min_difference[1]:
            pairs_min_difference[0], pairs_min_difference[1] = pairs_min_difference[1], pairs_min_difference[0]
            perfect_pairs[0], perfect_pairs[1] = perfect_pairs[1], perfect_pairs[0]

    if (perfect_pair != -1) and (perfect_pairs[1] != -1):
        if pair_min_difference <= pairs_min_difference[0] + pairs_min_difference[1]:
            print(f"Max sum is {min_in_pair_sum - data[perfect_pair][0] + data[perfect_pair][1]}")
        else:
            print(f"Max sum is {min_in_pair_sum - data[perfect_pairs[0]][0] - data[perfect_pairs[1]][0] + data[perfect_pairs[0]][1] + data[perfect_pairs[1]][1]}")
    elif perfect_pair != -1:
        print(f"Max sum is {min_in_pair_sum - data[perfect_pairs[0]][0] - data[perfect_pairs[1]][0] + data[perfect_pairs[0]][1] + data[perfect_pairs[1]][1]}")
    elif perfect_pairs[1] != -1:
        print(f"Max sum is {min_in_pair_sum - data[perfect_pair][0] + data[perfect_pair][1]}")
    else:
        print(f"Max sum is {0}")

elif min_in_pair_sum % 3 == 2:
    perfect_pair = -1
    pair_min_difference = 1000

    for number, pair in enumerate(data):
        if (pair[1] % 3) - (pair[0] % 3) == 1:
            if pair_min_difference > (pair[1] - pair[0]):
                perfect_min_difference = pair[1] - pair[0]
                perfect_pair = number

    perfect_pairs = [-1, -1]
    pairs_min_difference = [1000, 1000]

    for number, pair in enumerate(data):
        if (pair[1] % 3) - (pair[0] % 3) == 2:
            if pairs_min_difference[1] > (pair[1] - pair[0]):
                perfect_min_difference = pair[1] - pair[0]
                perfect_pairs[1] = number
        if pairs_min_difference[0] > pairs_min_difference[1]:
            pairs_min_difference[0], pairs_min_difference[1] = pairs_min_difference[1], pairs_min_difference[0]
            perfect_pairs[0], perfect_pairs[1] = perfect_pairs[1], perfect_pairs[0]

    if (perfect_pair != -1) and (perfect_pairs[1] != -1):
        if pair_min_difference <= pairs_min_difference[0] + pairs_min_difference[1]:
            print(f"Max sum is {min_in_pair_sum - data[perfect_pair][0] + data[perfect_pair][1]}")
        else:
            print(f"Max sum is {min_in_pair_sum - data[perfect_pairs[0]][0] - data[perfect_pairs[1]][0] + data[perfect_pairs[0]][1] + data[perfect_pairs[1]][1]}")
    elif perfect_pair != -1:
        print(f"Max sum is {min_in_pair_sum - data[perfect_pairs[0]][0] - data[perfect_pairs[1]][0] + data[perfect_pairs[0]][1] + data[perfect_pairs[1]][1]}")
    elif perfect_pairs[1] != -1:
        print(f"Max sum is {min_in_pair_sum - data[perfect_pair][0] + data[perfect_pair][1]}")
    else:
        print(f"Max sum is {0}")
