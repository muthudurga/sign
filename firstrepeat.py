N=int(input())
z=[int(z) for z in input().split()]
a=[]
for i in range(N):
    k=i+1
    for j in range(k,N):
        if z[i]==z[j]:
            if z[i] not in a:
                a.append(z[i])
if a==[]:
    print("unique")
else:
    print(a[0])
