# Грехов Александр 11-10

import math


def get_link_v(v, D):
    for i, weight in enumerate(D[v]):
        if weight > 0:
            yield i


def arg_min(T, S):
    amin = -1
    m = max(T)
    for i, t in enumerate(T):
        if t < m and i not in S:
            m = t
            amin = i
    return amin


def solution(graph):
    n = len(graph)
    t = [math.inf] * n
    start = 0  # Стартовая вершина
    viewed = {start}  # Просмотренные вершины
    t[start] = 0  # Нулевой вес для стартовой вершины

    while start != - 1:  # Цикл пока не просмотрим все вершины
        for j in get_link_v(start, graph):  # Перебираем все связанные вершины
            if j not in viewed:  # Если вершина ещё не посещена
                w = t[start] + graph[start][j]
                if w < t[j]:
                    t[j] = w
        start = arg_min(t, viewed)  # Выбираем следующий узел
        if start > 0:  # Выбрана очередная вершина
            viewed.add(start)  # Добавляем новую вершину

    return t


# Ациклический граф
ackl_g = ((0, 3, 1, 3, 0, 0),
          (3, 0, 4, 0, 0, 0),
          (1, 4, 0, 0, 7, 5),
          (3, 0, 0, 0, 0, 2),
          (0, 0, 7, 0, 0, 4),
          (0, 0, 5, 2, 4, 0))

# ЦИКЛИЧЕСКИЙ ГРАФ
ckl_g = ((0, 3, 0, 0, 0, 4),
         (3, 0, 5, 0, 0, 0),
         (0, 5, 0, 6, 0, 0),
         (0, 0, 6, 0, 7, 0),
         (0, 0, 0, 7, 0, 8),
         (4, 0, 0, 0, 8, 0))

# ГРАФ С ОТРИЦАТЕЛЬНЫМИ РЁБРАМИ
otr_g = ((0, -3, 1, 3, 0, 0),
         (-3, 0, -4, 0, 0, 0),
         (1, -4, 0, 0, -7, 5),
         (3, 0, 0, 0, 0, 2),
         (0, 0, -7, 0, 0, -4),
         (0, 0, 5, 2, -4, 0))

print('Для ациклического графа:')
print(solution(ackl_g), "\n")

print('Циклический граф:')
print(solution(ckl_g), "\n")


print('Граф с отрицательными рёбрами:')
print(solution(otr_g), "\n")
