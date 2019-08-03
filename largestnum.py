N=int(input())
z=[int(z) for z in input().split()]
for i in range(N):
    k=i+1
    for j in range(k,N):
        if z[i]<z[j]:
            temp=z[i]
            z[i]=z[j]
            z[j]=temp
y=''
for i in range(N):
    x=str(z[i])
    y=y+x
d=int(y)
print(d)
