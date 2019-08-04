N,K=[int(N) for N in input().split()]
if N>=K:
    x=[int(x) for x in input().split()]
    x.sort(reverse=True)
    for i in range(len(x)):
        c=K-1
        if i==c:
            print(x[i])
