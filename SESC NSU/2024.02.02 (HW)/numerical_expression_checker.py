# Грехов Александр 11-10


import re


def is_valid_expression(s):
    # Удаляем пробелы
    s = s.replace(' ', '')
    # Проверяем, что строка состоит только из допустимых символов
    if not re.match(r'^[0-9+\-()*]+$', s):
        return False
    # Проверяем, что скобки сбалансированы
    if s.count('(') != s.count(')'):
        return False
    # Проверяем, что нет двух операторов подряд
    if re.search(r'[+\-()]*[+\-]{2,}[+\-()]*', s):
        return False
    # Если все проверки пройдены, строка является правильным выражением
    return True


print(is_valid_expression('(13+4)*(-3+12)'))  # Вернет True
print(is_valid_expression('(6++3'))  # Вернет False
