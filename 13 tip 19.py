def F(x,y,h):
    if x+y>=62 and h==3:
        return 1
    if x+y<62 and h==3:
        return 0
    return F(x+1,y,h+1) or F(x*2,y,h+1) or F(x,y+1,h+1) or F(x,y*2,h+1)
for y in range(1,52):
    if F(10,y,1)==1:
        print(y)
        break
    #answer: 13           