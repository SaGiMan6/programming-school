# Задание 1

# Имеется набор данных, состоящий из пар положительных целых чисел.
# Необходимо выбрать из каждой пары ровно одно число так,
# Чтобы сумма всех выбранных чисел делилась на 2 и при этом была максимально возможной.
# Если получить требуемую сумму невозможно, в качестве ответа нужно выдать 0.


from random import randint


data = []

# Генерируем количество чисел, указанное пользователем
n = int(input("How many pairs you want to check? ").strip())
for i in range(n):
    data.append([randint(1, 100), randint(1, 100)])


max_in_pair_sum = 0

# Делаем так, чтобы первым в паре было максимальное число пары, вторым - минимальное
for number, pair in enumerate(data):
    min_in_pair = min(pair[0], pair[1])
    max_in_pair = max(pair[0], pair[1])
    data[number] = [max_in_pair, min_in_pair]

    max_in_pair_sum += max_in_pair


# Проверяем, делится ли сумма первых чисел пар на 2

# Если сумма не делится на 2, ищем пару с минимальной разницей чисел,
# Где одно из чисел делится на 2, а второе не делится на 2
# Из такой пары мы берем меньшее число и тогда сумма меняется наименьшим образом и делится на 2

# Если нет такой пары, где одно из чисел делится на 2, а второе не делится, выводим 0,
# Так как невозможно получить сумму, делящуюся на 2
if max_in_pair_sum % 2 != 0:
    perfect_min_difference = 1000
    perfect_pair = -1

    for number, pair in enumerate(data):
        if pair[0] % 2 != pair[1] % 2:
            if perfect_min_difference > (pair[0] - pair[1]):
                perfect_min_difference = pair[0] - pair[1]
                perfect_pair = number

    if perfect_pair != -1:
        print(f"Max sum is {max_in_pair_sum - data[perfect_pair][0] + data[perfect_pair][1]}")
    else:
        print(f"Max sum is {0}")
else:
    print(f"Max sum is {max_in_pair_sum}")
