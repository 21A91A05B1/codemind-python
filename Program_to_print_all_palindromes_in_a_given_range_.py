a=int(input())
b=int(input())
for i in range(a,b+1,1):
    num=i
    r=0
    while(num>0):
        d=num%10
        num=num//10
        r=r*10+d
    if(r==i)    :
        print(i,end=' ')
