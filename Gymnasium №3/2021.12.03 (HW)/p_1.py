x=int(input())
ch=0
chx=0
y=0
while x!=100:
    ch+=1
    if x==77:
        y=1
    if chx==0:
        if x==77:
            chx=ch
    x=int(input())
if y==0:
    print ("В последовательности не было числа 77")
else:
    print ("В последоваетльности было число 77")
    if chx!=0:
        print ("Первый раз число 77 встертилов на вводе №", chx)