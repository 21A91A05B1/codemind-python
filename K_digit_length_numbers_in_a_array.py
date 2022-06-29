n,m=map(int,input().split())
a=list(map(int,input().split()))
c=0
for i in a:
    if(i<0):
        i=(-i)
    if(len(str(i))==m):
        c+=1
print(c)        