x = int(input())
y = 0
ch = 0

while x != 0:
    if x // 100 == 0 and x % 100 >= 10:
        y += x
        ch += 1
    x = int(input())

if ch > 0:
    print(y/ch)
