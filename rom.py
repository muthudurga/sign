def rom():
        rom={'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        x=input()
        s=0
        for i in range(len(x)):
            if i > 0 and rom[x[i]] > rom[x[i - 1]]:
                s+= rom[x[i]] - 2 * rom[x[i - 1]]
            else:
                s+= rom[x[i]]
        print(s)
rom()


