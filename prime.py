def prime():
    if x>1:
        for i in range(2,x):
            if x%i==0:
                print('no')
                break
        else:
            print('yes')
    else:
        print('no')
x=int(input())
prime()
