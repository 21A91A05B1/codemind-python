n=int(input())
arr=[]
list=map(int,input().split())
for i in list:
    if i not in arr:
        arr.append(i)
print(*arr)        
        