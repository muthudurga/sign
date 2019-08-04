n=[int(n) for n in input().split()]
x=[int(x) for x in input().split()]
z=[]
if len(n)==len(x):
    for i in range(len(n)):
        z.append(n[i]-x[i])
print(*z)
