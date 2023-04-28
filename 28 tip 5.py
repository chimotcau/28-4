for n in range(1000,0,-1):
    s= format(n,'b')
    if n%2==0:
        s= s+'00'
    else:
        s= s+'11'
    r= int(s,2)
    if r<134:
        print(n)
        break
    #answer:32

