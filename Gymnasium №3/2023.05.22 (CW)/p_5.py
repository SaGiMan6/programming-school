# Задание: "Словарь 4"

s = '1:men 2:kind 90:number 0:sun 34:book 56:mountain 87:wood 54:car 3:island 88:power 7:box 17:star 101:ice'.split()


result = {int(value[:value.rfind(":")]): value[value.rfind(":") + 1:] for value in s}


for key in result:
    print(f"{key}: {result[key]}")
