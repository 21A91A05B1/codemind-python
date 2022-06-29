n,m=map(int,input().split())
a1=list(map(int,input().split()))
a2=list(map(int,input().split()))
a=[]
b=[]
for i in a1:
    if i in a2:
        a.append(i)
for i in a:
    if i not in b:
        b.append(i)
print(*b)        
         