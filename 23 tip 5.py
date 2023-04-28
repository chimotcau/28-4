for n in range(1,10000):
    s = format(n,'b')
    s = s+ str(s.count('1')%2)
    s = s+ str(s.count('1')%2)
    r = int(s,2)
    if r>85:
        print(n)
        break
    #answer:21

