for n in range(1,10000):
    s = format(n,'b')
    if (s.count('1'))>(s.count('0')):
        s =s +'1'
    if (s.count('0'))>=(s.count('1')):
        s = s+'0'
    r = int(s,2)
    if r >80:
        print(r)
        break
    #answer: 82        
        
