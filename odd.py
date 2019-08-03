N,Q=[int(N) for N in input().split()]
z=''
for i in range(N+1,Q):
    for x in range(N+1,Q):
        if i%x==0:
            break
        else:
            z=z+str(i)+' '
            break
print(z)
            
