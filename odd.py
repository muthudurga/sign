N,Q=[int(N) for N in input().split()]
z=[]
for i in range(N+1,Q):
    if i%2!=0:
        z.append(i)
print(*z)
            
