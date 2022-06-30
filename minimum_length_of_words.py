s=input()
s=s.split(" ")
min=999
for i in s:
    m=len(i)
    if(min>m):
        min=m
print(min)     