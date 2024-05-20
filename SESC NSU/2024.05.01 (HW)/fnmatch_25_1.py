# Решение 25 задачи ЕГЭ с помощью fnmatch (1)

import fnmatch


max_num = 10**10 // 4891

for i in range(1, max_num + 1):
    if fnmatch.fnmatch(str(i * 4891), "1?7602*0"):
        print(i * 4891)
