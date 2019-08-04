N,M=[int(N) for N in input().split()]
A=[int(A) for A in input().split()]
B=[int(B) for B in input().split()]
x=[]
if M<=N:
    for i in range(M):
        
        if B[i] in A:
             x.append(B[i])
if B==x:
    print("YES")
else:
    print("NO")
