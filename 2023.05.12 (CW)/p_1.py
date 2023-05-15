wrds = input().split()
slv = dict()


for wrd in wrds:
    if wrd in slv:
        print(slv[wrd], end=" ")
        slv[wrd] += 1
    else:
        print(0, end=" ")
        slv[wrd] = 1
