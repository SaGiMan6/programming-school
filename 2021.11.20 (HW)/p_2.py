x=int(input())
a=0
b=0
while x!=0:
    if x%10==0:
        a+=1
    if x%10==9:
        b+=1
    x//=10
if a>b:
    print("Нулей больше")
else:
    if a<b:
        print("Девяток больше")
    else:
        print("Равное количество нулей и девяток")