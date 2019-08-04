n=int(input())
x=0
y=1
a=[]
for i in range(1,n+2):
    if x!=0:
        a.append(x)
    z=x+y
    x=y
    y=z
print(*a)
    
