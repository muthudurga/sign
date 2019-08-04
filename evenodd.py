N=int(input())
x=[int(x) for x in input().split()]
s=[]
for i in range(N):
    if i%2==0:
        if x[i]%2!=0:
            s.append(x[i])
    else:
        if x[i]%2==0:
            s.append(x[i])
print(*s)
