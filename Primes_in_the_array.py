def isprime(n):
    if(n==1):
        return 0
    for i in range(2,n):
        if(n%i==0):
            break
    else:
        return 1
n=int(input())    
a=list(map(int,input().split()))
c=0
sum=0
for i in a:
    if(isprime(i)==1):
        c+=1
print(c)        