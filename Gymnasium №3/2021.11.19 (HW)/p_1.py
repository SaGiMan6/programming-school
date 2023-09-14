a=int(input())
summ=0
while (a*10)//10!=0:
    summ+=(a%10)**2
    a//=10
    print (a)
    print (summ)
print(summ)