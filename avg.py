N=int(input())
x=[int(x) for x in input().split()]
s=0
if len(x)==N:
    for i in range(len(x)):
        s=s+x[i]
    a=s/N
    print(int(a))
