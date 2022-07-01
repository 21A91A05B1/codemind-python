n,k=map(int,input().split())
arr=list(map(int,input().split()))
c=0
a=[]
for i in arr:
    if(i<0):
        i=-1
    if(i%k==0):
        c+=1
print(c)        
    
