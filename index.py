n=int(input())
x=[int(x) for x in input().split()]
z=[]
for i in range(len(x)):
    if i==x[i]:
        z.append(x[i])
if z==[]:
    print(-1)
else:
    print(*z)
