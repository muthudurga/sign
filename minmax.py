N=int(input())
x=[int(x) for x in input().split()]
z=[]
if len(x)==N:
    z.append(min(x))
    z.append(max(x))
print(*z)
