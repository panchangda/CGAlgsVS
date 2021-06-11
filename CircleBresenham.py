def generatePoints(r):
    pointlist = []
    # if(r<=0):
    #     return pointlist
    x = 0
    y = r
    delta = 2*(1-r)
    limit = 0
    
    #1/4 Circle
    while y >= limit:

        pointlist.append([x, y])

        #
        if delta < 0:
            delta1 = 2*(delta+y)-1
            if delta1 <= 0:
                direction = 1
            else:
                direction = 2
        elif delta > 0:
            delta2 = 2*(delta-x)-1
            if delta2 < 0:
                direction = 2
            else:
                direction = 3
        else:
            direction = 2

        if direction == 1:
            x += 1
            delta += 2*x+1
        elif direction == 2:
            x += 1
            y-= 1
            delta += 2*(x-y+1)
        elif direction == 3:
            y-=1
            delta += (-2*y+1)

    for i in range (len(pointlist)):
        [x,y] = pointlist[i]
        pointlist.append([-x,y])
        pointlist.append([-x,-y])
        pointlist.append([x,-y])
        
    return pointlist
