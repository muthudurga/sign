n=input()
sum=0

for i in range(len(n)):
    if(n[i].isalpha()):
        sum=sum+0
    elif(n[i].isdigit()):
        sum=sum+0
    else:
        sum=sum+1
print(sum)
