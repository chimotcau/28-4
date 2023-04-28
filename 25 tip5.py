for n in range(1,1000):
    s= format(n,'b')
    if s.count('1')%2==0:
        s= s +'1'
    else:
        s= s+'0'
    if s.count('1')%2==0:
        s= s +'1'
    else:
        s= s+'0'
    r = int(s,2)
    if r>54:
        print(r)
        break
    #answer:  56      

