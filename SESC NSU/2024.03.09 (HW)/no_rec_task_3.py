# Грехов Александр 11-10

def combinations(al, n, start=0, prefix=''):
    stack = [(al, n, start, prefix)]
    while stack:
        al, n, start, prefix = stack.pop()
        if n == 0:
            print(prefix, end='\n')
        else:
            for i in range(len(al) - 1, start - 1, -1):
                new_prefix = prefix + al[i]
                stack.append((al, n - 1, i + 1, new_prefix))


N = 2
M = 3
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

combinations(alphabet[:M], N)
