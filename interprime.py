N,Q=[int(N) for N in input().split()]
z=[]
for num in range(N,Q):  
   if num > 1:  
       for i in range(2,num):  
           if (num % i) == 0:  
               break  
       else:  
           z.append(num)
print(*z)
