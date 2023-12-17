# В программу подается набор из N строк, состоящих из 0 и 1, удовлетворяющее условию Фано.
# Добавить в это множество минимальную строку, такую, что соблюдение условия Фано сохранится.

def check_fano_condition(strings, string):
    for i in range(len(strings)):
        if strings[i] == string or strings[i].startswith(string) or string.startswith(strings[i]):
            return False
    return True


def add_minimal_string(strings, k: int = 1):
    new_strings = []
    while len(new_strings) < k:
        min_str = ""

        for i in range(1, 4):
            for j in range((2 ** i) + 1):
                min_str = bin(j)[2:]
                if len(min_str) < i:
                    min_str = (i - len(min_str)) * "0" + min_str

                if check_fano_condition(strings, min_str):
                    new_strings.append(min_str)
                    strings.append(min_str)
                else:
                    min_str = ""

                if min_str != "":
                    break

            if min_str != "":
                break

    return new_strings


n = int(input("Введите количество строк (длинна строк до 20 символов): "))

input_strings = ["" for _ in range(n)]
for i in range(n):
    input_strings[i] = input()

minimal_string = add_minimal_string(input_strings)
if minimal_string:
    print("Минимальная строка для сохранения условия Фано:", *minimal_string)
else:
    print("Невозможно добавить минимальную строку")
