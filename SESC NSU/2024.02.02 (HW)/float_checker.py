# Грехов Александр 11-10

# В ходе решения этого задания, я считаю что целое число тоже действительное.
# Программу можно легко поменять, заменив в 9 строке ">" на "!=".
# Тогда программа не будет считать целое число действительным


def is_float(s):
    if s.count('.') > 1:  # Если в строке больше одной точки, это не float
        return False

    if s[0] in ("+", "-"):
        s = s[1:]
    s.replace('.', '', 1)

    for char in s:
        if str(char) not in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"):
            return False

    return True


string = input("Введите строку: ")
print(is_float(string))
