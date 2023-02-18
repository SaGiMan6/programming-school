print(141)


from random import randint


P = []
Q = []


for i in range(12):
    P.append(randint(-10,10))
for i in range(12):
    Q.append(0)

for i in range(12):
    if 3 <= i < 10:
        Q[i] = -1 * P[i]
    else:
        Q[i] = P[i]*i


print(P)
print(Q)

