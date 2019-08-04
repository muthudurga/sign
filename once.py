n=int(input())
x=[int(x) for x in input().split()]
z=[]
for i in range(len(x)):
    if x[i] not in z:
        z.append(x[i])
    else:
        z.remove(x[i])
print(*z)
        
    
