for n in range(1,10000):
    s= format (n,'b')
    if s[-1] == '0':
        s= '1' +s +'0'
    else:
        s = '11' + s + '11'
    r = int(s,2)
    if r>52:
        print(n)
        break
    #answer: 3   