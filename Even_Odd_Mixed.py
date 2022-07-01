n=int(input())
es=0
os=0
c=0
while(n):
    d=n%10
    c+=1
    n=n//10
    if(d%2==0):
        es+=1
    else:
        os+=1
if c==es:
    print("Even")
elif c==os:
    print("Odd")
else:
    print("Mixed")