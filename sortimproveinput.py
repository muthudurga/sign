N=int(input())
x=[int(x) for x in input().split()]
if len(x)==N:
    x.sort()
    print(*x)
