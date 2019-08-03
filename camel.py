x=input()
y=''
i=0
a=0
for i in range(len(x)):
    if x[i]!=' ':
        if i==0:
            y=y+x[i].upper()
        elif i==a:
            continue
        else:
            y=y+x[i].lower()
    else:
        y=y+x[i]+x[i+1].upper()
        a=i+1
print(y)
