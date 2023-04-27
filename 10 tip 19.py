def F( x,y,h):
    if x +y <= 40 and h == 3:
        return True
    if x + y >40 and h ==3:
        return False
    return F(x-1,y,h+1) or F(x//2,y,h+1) or F(x,y-1,h+1) or F(x,(y+1)//2,h+1)
for s in range(100,20,-1):
    if F(20,s,1) == True:
        print(s)
        break
    #answer:80                

            
