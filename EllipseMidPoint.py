
def generatePoints(a, b):
    # a=abs(a)
    # b=abs(b)

    pointlist = []
    d = b**2 + a**2*(0.25-b)
    x = 0
    y = b
    
    # 上半部分
    while(b**2*(x+1) < a**2*(y-0.5)):  
        pointlist.append([x, y])
        if(d <= 0):
            d += b**2*(2*x+3)
            x += 1
        else:
            d += (b**2*(2*x+3)+a**2*(-2*y+2))
            x += 1
            y -= 1

    # 进入下半部分
    d = b**2*(x+0.5)**2+a**2*(y-1)**2-a**2*b**2
    while(y >= 0):
        pointlist.append([x, y])
        if(d > 0):
            d += a**2*(-2*y+3)
            y -= 1
        else:
            d += (b**2*(2*x+2)+a**2*(-2*y+3))
            y -= 1
            x += 1

    for i in range(len(pointlist)):
        [x, y] = pointlist[i]
        pointlist.append([x, -y])
        pointlist.append([-x, -y])
        pointlist.append([-x, y])

    return pointlist
