# К задаче не прилагались файлы, так что я нашел файлы для аналогичной задачи
# Ответ к файлу A – 51063
# Ответ к файлу B – 5634689219329

with open("27_lab_B.txt") as file:
    lines = file.read().split("\n")

n = int(lines[0])

pre_data = []
for line in lines[1:]:
    pre_data.append(list(map(int, line.split())))
pre_data.sort(key=lambda x: x[0])

k = (pre_data[-1][0] + 1)
data = [0] * k
for line in pre_data:
    data[line[0]] = (line[1] + 35) // 36


s = 0
for i in range(1, k):
    s += data[i] * i

if data[0] > 0:
    min_s = s
else:
    min_s = 10**20


total = sum(data)
s_right = sum(data[1:])
s_left = total - s_right

for i in range(1, k):
    s = s - s_right + s_left
    s_right -= data[i]
    s_left = total - s_right

    if data[i] > 0:
        min_s = min(min_s, s)


print(min_s)
