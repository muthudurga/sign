N=int(input())
x=[int(x) for x in input().split()]
if N==len(x):
    for i in range(len(x)):
        print(x[i],i)
