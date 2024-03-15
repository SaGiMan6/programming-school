# Грехов Александр 11-10


# Создаём матрицу смежности
matrix = [(13, 1, 2), (18, 1, 3), (17, 1, 4),
          (14, 1, 5), (22, 1, 6), (26, 2, 3),
          (22, 2, 5), (3, 3, 4), (19, 4, 6)]

sort_m = sorted(matrix, key=lambda x: x[0])
connected_h = set()  # список соединённых вершин
isolated_groups = {}  # словарь списка изолированных групп вершин
T = []  # Список рёбер остова

for r in sort_m:
    if r[1] not in connected_h or r[2] not in connected_h:  # Проверка для исключения циклов в остове
        if r[1] not in connected_h and r[2] not in connected_h:  # Если обе вершины не соединены
            isolated_groups[r[1]] = [r[1], r[2]]  # Формируем в словаре ключ с номерами вершин
            isolated_groups[r[2]] = isolated_groups[r[1]]  # Связываем их с одним и тем же списком вершин
        else:
            if not isolated_groups.get(r[1]):  # Если в словаре нет первой вершины
                isolated_groups[r[2]].append(r[1])  # Добавляем в список первую вершину
                isolated_groups[r[1]] = isolated_groups[r[2]]  # Добавляем ключ с номером первой вершины
            else:  # По аналогии со второй вершиной
                isolated_groups[r[1]].append(r[2])
                isolated_groups[r[2]] = isolated_groups[r[1]]
        T.append(r)  # Добавляем ребро в остов
        connected_h.add(r[1])  # Добавляем вершину в множество U
        connected_h.add(r[2])  # Добавляем вершину в множество U

for r in sort_m:  # Проходим по рёбрам второй раз и соединяем разрозненные группы вершин
    if r[1] in isolated_groups[r[1]] and r[2] not in isolated_groups[r[1]]:  # Если вершины принадлежат разным
        # группам, то объединяем
        T.append(r)  # Добавляем ребро в остов
        gr1 = isolated_groups[r[1]]
        isolated_groups[r[1]] += isolated_groups[r[2]]  # Объединяем списки двух групп вершин
        isolated_groups[r[2]] += gr1


print('Для данного графа: ')
print(matrix)
print('Минимальным остовом будет: ')
print(T)
