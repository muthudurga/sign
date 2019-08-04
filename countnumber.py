n=input()
sum=0
for i in range(len(n)):
    try:
        int(n[i])
        sum=sum+1
    except ValueError:
        sum=sum+0
print(sum)
