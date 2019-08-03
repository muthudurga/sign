x=input()
y=''
if len(x)%2==0:
    for i in range(0,len(x),2):
        y=y+x[i+1]+x[i]
else:
    for i in range(0,len(x)-1,2):
        y=y+x[i+1]+x[i]
    y=y+x[i+2]
print(y)
