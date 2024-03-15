# Грехов Александр 11-10

import math


def floyd_warshall(graph):
    # В этом коде graph - это матрица смежности
    n = len(graph)
    dist = list(map(lambda i: list(map(lambda j: j, i)), graph))

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    # После выполнения этого кода,
    # dist[i][j] будет содержать кратчайшее расстояние между вершинами i и j
    return dist


# Матрица смежности
matrix = [[0, 2, math.inf, 3, math.inf, math.inf, math.inf, 10],
          [2, 0, 4, math.inf, math.inf, math.inf, math.inf, math.inf],
          [math.inf, 4, 0, math.inf, math.inf, math.inf, math.inf, 3],
          [3, math.inf, math.inf, 0, math.inf, math.inf, math.inf, 8],
          [math.inf, math.inf, math.inf, math.inf, 0, 2, math.inf, math.inf],
          [math.inf, math.inf, math.inf, math.inf, 2, 0, 3, math.inf],
          [math.inf, math.inf, math.inf, math.inf, math.inf, 3, 0, math.inf],
          [10, math.inf, 3, 8, math.inf, math.inf, math.inf, 0]]

print(floyd_warshall(matrix))
