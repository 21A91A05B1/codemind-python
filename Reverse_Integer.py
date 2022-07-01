n=int(input())
t=n
r=0
num=abs(n)
t=num
if(n>0):
    while(n>0):
        d=n%10
        n=n//10
        r=r*10+d
else:
    while(num>0):
        d=num%10
        num=num//10
        r=r*10+d
    r=-(r)    
print(r)    
    
    