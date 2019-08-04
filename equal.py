N,A,B=[int(N) for N in input().split()]
if N%2==0:
    c=A+B
    d=N/2
    if d%c==0 or c%d==0:
        print("YES")
    else:
        print("NO")
else:
    print("NO")
