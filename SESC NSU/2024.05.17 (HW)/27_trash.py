# Ответ к файлу A – 8
# Ответ к файлу B – 41495

with open("27_trash_A.txt") as file:
    lines = list(map(int, file.read().split("\n")))

n = lines[0]
data = lines[1:]

total = sum(data)
s = 0

s += (n // 2) * data[n // 2]
for i in range(1, n // 2):
    s += i * (data[i] + data[n - i])

s_right = sum(data[1:n // 2 + 1])
s_left = total - s_right

min_s = s
min_ind = 0

for i in range(1, n):
    s = s - s_right + s_left
    s_right = s_right - data[i] + data[(i + (n // 2)) % n]
    s_left = total - s_right

    if s < min_s:
        min_s = s
        min_ind = i

print(min_ind + 1)
