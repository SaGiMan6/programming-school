print(143)


from random import randint


P = []
Q = []


for i in range(12):
    P.append(randint(-10,10))
for i in range(12):
    Q.append(0)

for i in range(12):
    if i % 2 == 0:
        Q[i] = P[i]
    else:
        Q[i] = P[i]*2


print(P)
print(Q)
