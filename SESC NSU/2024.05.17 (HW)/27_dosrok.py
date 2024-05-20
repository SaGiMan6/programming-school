# Ответ к файлу A – 129086
# Ответ к файлу B – 15233987675003

with open("27_dosrok_A.txt") as file:
    lines = file.read().split("\n")

n, k = map(int, lines[0].split())
pre_data = lines[1:]

size = 11
data = [0] * k
for line in pre_data:
    temp = list(map(int, line.split()))
    data[temp[0]] = (temp[1] + (size - 1)) // size

s = 0
total = sum(data)
s_right = sum(data[1: (k // 2) + 1])
s_left = total - s_right

s += (k // 2) * data[(k // 2)]
for i in range(1, k // 2):
    s += i * (data[i] + data[k - i])

min_s = s

for i in range(1, k):
    s = s - s_right + s_left
    s_right = s_right - data[i] + data[(i + (k // 2)) % k]
    s_left = total - s_right

    if data[i] > 0 and s < min_s:
        min_s = s

print(min_s)