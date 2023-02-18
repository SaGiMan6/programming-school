x=int(input())
ch=0
chx=0
y=x
while x!=(-1):
    ch+=1
    if y==x:
        chx=ch
    if y>x:
        y=x
        chx=0
    x=int(input())
print("Наименьшее число в последовательности", y)
if chx!=0:
    print ("Последний раз это число встречалось на вводе №", chx)