# Решение 25 задачи ЕГЭ с помощью fnmatch (2)

import fnmatch


max_num = 10**8 // 317

for i in range(1, max_num + 1):
    if fnmatch.fnmatch(str(i * 317), "12??1*56"):
        print(i * 317)
