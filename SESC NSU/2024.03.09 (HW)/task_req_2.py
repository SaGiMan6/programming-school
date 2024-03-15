def generate_permutation(K, N, M):
    """
    Генерирует К-е размещение в словарном порядке из первых M букв латинского алфавита.

    :param K: Порядковый номер размещения (1-based).
    :param N: Длина размещения.
    :param M: Количество букв в алфавите (M <= 26).
    :return: Сгенерированное размещение.
    """
    if N == 0:
        return ""

    # Вычисляем количество размещений, начинающихся с каждой буквы
    permutations_per_letter = [1] * M
    for i in range(1, M):
        permutations_per_letter[i] = permutations_per_letter[i - 1] * (N - i)

    # Находим букву, которая будет первой в размещении
    first_letter_index = 0
    while K > permutations_per_letter[first_letter_index]:
        K -= permutations_per_letter[first_letter_index]
        first_letter_index += 1

    # Рекурсивно генерируем оставшуюся часть размещения
    remaining_permutation = generate_permutation(K, N - 1, M)

    # Преобразуем индекс буквы в символ
    first_letter = chr(ord('A') + first_letter_index)

    # Собираем размещение
    return first_letter + remaining_permutation

# Пример использования:
K = 10  # Порядковый номер размещения
N = 4   # Длина размещения
M = 3   # Количество букв в алфавите (A, B, C)
result_permutation = generate_permutation(K, N, M)
print(f"Размещение {K}-е в словарном порядке: {result_permutation}")
