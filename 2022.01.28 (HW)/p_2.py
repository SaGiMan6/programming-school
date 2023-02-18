print(142)


from random import randint


P = []
Q = []
V = []


for i in range(12):
    P.append(randint(-10,10))
for i in range(12):
    Q.append(0)

for i in range(0, 12, 2):
    Q[i] = P[i]

for i in range(0, 12, 2):
    V.append(P[i])


print(P)
print(Q)
print(V)