with open("27_dosrok_0.txt") as file:
    lines = file.read().split("\n")
    n, k = map(int, lines[0].split())
    pre_data = lines[1:]

road = [0] * k
for line in pre_data:
    temp = list(map(int, line.split()))
    road[temp[0] - 1] = temp[1]

size = 3
fst_b = list(map(int, pre_data[0]))[0]

for v in range(n)
    
