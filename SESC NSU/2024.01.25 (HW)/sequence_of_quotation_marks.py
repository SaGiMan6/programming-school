# Грехов Александр 11-10


def is_correct_brackets(sequence):
    while '\'\'' in sequence or '\"\"' in sequence:
        sequence = sequence.replace('\'\'', '')
        sequence = sequence.replace('\"\"', '')

    return not sequence


text = input('Введите скобочную последовательность: ')

print(is_correct_brackets(text))
