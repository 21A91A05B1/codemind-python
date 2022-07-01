n=int(input())
arr=list(map(int,input().split()))
c=0
a=[]
for i in arr:
    a.append(len(str(i)))
m=max(a)    
for i in arr:
    if(len(str(i))==m):
        c+=1
print(c)        
