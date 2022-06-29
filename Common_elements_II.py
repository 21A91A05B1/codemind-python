n,m=map(int,input().split())
a1=list(map(int,input().split()))
a2=list(map(int,input().split()))
a=[]
b=[]
for i in a1:
    if i not in a2:
        a.append(i)
for i in a2:
    if i not in a1:
        b.append(i)
c=list(a)+list(b)        
print(*c)