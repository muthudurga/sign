N,Q=[int(N) for N in input().split()]
z=[]
for i in range(N+1,Q):
    for x in range(N+1,Q):
        if i%x==0:
            z.append(i)
            break
        else:
            break
print(*z)
            
