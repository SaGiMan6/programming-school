x = int(input())
ch = 0

for i in range(x):
    a = int(input())
    if a % 3 == 0 and a % 10 == 2:
        ch += 1

print(ch)
