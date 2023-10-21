# Задание 4.

# Сгенерировать длинную последовательность данных (не менее 200 чисел),
# состоящих из цифр [1, 2, 3].
# Воспользоваться случайными числами.

# Написать программу, которая находит самую длинную непрерывную подпоследовательность,
# состоящую из троек.

from random import randint


data = []

# Генерируем количество чисел, указанное пользователем
n = int(input("How many numbers you want to check? ").strip())
for i in range(n):
    data.append(randint(1, 3))


sequence_max = 0

data_max = 0
data_max_borders = []

# Проходим массив чисел, ищем последовательности '3'
# Если последовательность больше предыдущей максимальной, сохраняем длину и границы
for number, element in enumerate(data):
    if element == 3 and data[number - 1] == 3:
        sequence_max += 1
    elif element == 3 and data[number - 1] != 3:
        sequence_max = 1

    if sequence_max > data_max:
        data_max = sequence_max
        data_max_borders = [number - (data_max - 1), number]


# Выводим результат
print(f"Max sequence of '3' is {data_max}")
print(f"The indexes of max sequence are {data_max_borders}")
