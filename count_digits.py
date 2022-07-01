n=int(input())
arr=list(map(int,input().split()))
c=0
a=[]
for i in arr:
    if(i<0):
        i=-i
    a.append(len(str(i)))    
print(*a)    