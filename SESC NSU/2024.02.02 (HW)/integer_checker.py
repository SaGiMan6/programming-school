# Грехов Александр 11-10


# Способ №1 (Лаконичный)
def is_integer_lcn(s):
    if s[0] in ('-', '+'):
        return s[1:].isdigit()
    return s.isdigit()


# Способ №2 (Без оператора определяющего число)
def is_integer_stp(s):
    if s[0] in ('-', '+'):
        s = s[1:]

    for char in s:
        if str(char) not in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"):
            return False

    return True


string = input("Введите строку: ")
print("Лаконичный способ:", is_integer_lcn(string))
print("Способ без оператора", is_integer_stp(string))
