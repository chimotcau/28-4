def f(x,y,h):
    if x+y>=75 and h==3:
        return 1
    if x+y<75 and h==3:
        return 0
    return f(x+1,y,h+1) or f(x,y+1,h+1) or f(x+y,y,h+1) or f(x,y+x,h+1)
for y in range(1,68):
    if f(7,y,1)==1:
        print(y)
        break
    #answer:21            