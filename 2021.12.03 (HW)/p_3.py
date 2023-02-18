x=int(input())
cha=0
chb=0
while x!=0:
    if x!=1:
        d=x-1
    else:
        d=1
    while x%d!=0:
        d-=1
    if d==1:
        cha+=1
    else:
        chb+=1
    x=int(input())
print ("В последовательности", cha, "простых чисел")
print ("В последовательности", chb, "составных чисел")
