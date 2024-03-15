def generate_word(K, N, M):
    """
    Генерирует К-е слово в словарном порядке из первых M букв латинского алфавита.

    :param K: Порядковый номер слова (1-based).
    :param N: Длина слова.
    :param M: Количество букв в алфавите (M <= 26).
    :return: Сгенерированное слово.
    """
    if N == 0:
        return ""

    # Вычисляем количество слов, начинающихся с каждой буквы
    words_per_letter = [1] * M
    for i in range(1, M):
        words_per_letter[i] = words_per_letter[i - 1] * (N - 1 + i) // i

    # Находим букву, которая будет первой в слове
    first_letter_index = 0
    while K > words_per_letter[first_letter_index]:
        K -= words_per_letter[first_letter_index]
        first_letter_index += 1

    # Рекурсивно генерируем оставшуюся часть слова
    remaining_word = generate_word(K, N - 1, M)

    # Преобразуем индекс буквы в символ
    first_letter = chr(ord('A') + first_letter_index)

    # Собираем слово
    return first_letter + remaining_word

# Пример использования:
K = 10  # Порядковый номер слова
N = 4   # Длина слова
M = 3   # Количество букв в алфавите (A, B, C)
result_word = generate_word(K, N, M)
print(f"Слово {K}-е в словарном порядке: {result_word}")