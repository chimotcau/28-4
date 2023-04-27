def f(x,y,h):
    if x+y>= 91 and h==3:
        return 1
    if x+y<91 and h==3:
        return 0
    return f(x+1,y,h+1) or f(x*4,y,h+1) or f(x,y+1,h+1) or f(x,y*4,h+1)
for y in range(1,86):
    if f(5,y,1)==1:
        print(y)
        break
    #answer:6            