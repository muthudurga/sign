N,Q=[int(N) for N in input().split()]
z=[]
for n in range(N+1,Q): 
    temp=n
    s=0
    while(n!=0):
        r=n%10
        c=r**3
        s=s+c
        n=n//10
    if s==temp:
        z.append(s)
print(*z)

