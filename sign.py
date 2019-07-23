def sign():
    a=1
    while(a>0):
        n=input( )
        try:
            x=int(n)
            if x>0:
                print("Positive")
            elif x<0:
                print("Negative")
            else:
                print("Zero")
        except:
            print(n+" is not a number")
sign()
    
