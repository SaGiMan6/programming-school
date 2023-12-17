# В программу поступает N строк, состоящих из 0 и 1.
# Проверить их набор на соблюдение условия Фано,
# т.е. ни одна строка не является началом любой другой из этих строк.

def check_fano_condition(strings):
    for i in range(len(strings)):
        for j in range(len(strings)):
            if i != j and strings[i].startswith(strings[j]):
                return False
    return True


n = int(input("Введите количество строк: "))

input_strings = ["" for _ in range(n)]
for i in range(n):
    input_strings[i] = input()

if check_fano_condition(input_strings):
    print("Условие Фано выполнено")
else:
    print("Условие Фано не выполнено")
