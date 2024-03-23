def generate_word(k, m, n):
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
k = int(input("Введите порядковый номер слова"))
m = int(input("Введите количество букв в алфавите"))
n = int(input("Введите длину искомого слова"))

result_word = generate_word(k, m, n)
print(f"Слово {k}-е в словарном порядке: {result_word}")
