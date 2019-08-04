n,q=input().split()
x=len(n)
y=len(q)
c=max(x,y)
if c==x and c==y:
    print(n or q)
elif c==x:
    print(n)
else:
    print(q)
