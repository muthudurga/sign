N=int(input())
x=[int(x) for x in input().split()]
if N==len(x):
    x.sort()
    print(*x)
