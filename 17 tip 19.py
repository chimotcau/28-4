def f(x,y,h):
    if x+y>=45 and h==3:
        return 1
    if x+y<45 and h==3:
        return 0
    return f(x+1,y,h+1)or f(x*3,y,h+1) or f(x,y+1,h+1) or f(x,y*3,h+1)
for y in range(1,41) :
    if f(4,y,1)==1:
        print(y)
        break
    #answer: 5          