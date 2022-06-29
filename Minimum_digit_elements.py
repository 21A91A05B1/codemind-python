n=int(input())
a=list(map(str,input().split()))
b=[]
c=0
for i in a:
    b.append(len(i))
m=min(b)    
for i in a:
    if(len(i)==m):
        c+=1
print(c)        