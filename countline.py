n=input()
sum=1
for i in range(len(n)):
    if i!=(len(n)-1):
        if n[i]=='.':
            sum=sum+1
if n=='':
    sum=0
print(sum)
