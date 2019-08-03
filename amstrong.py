n=int(input())
temp=n
s=0
while(n!=0):
    r=n%10
    c=r**3
    s=s+c
    n=n//10
if s==temp:
    print("yes")
else:
    print("no")
