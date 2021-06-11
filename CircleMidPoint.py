
def generatePoints(r):
    pointlist = []
    # if(r<=0):
    #     return pointlist
    x = 0
    y = r
    #d = F(x+1,y-0.5) = x^2 + y^2 -R^2
    #d0 = F(1,R-0.5)
    d = 1.25 -r 

 
    while(x<=y):
        pointlist.append([x,y])
        if d<0:
            #point in Circle
            #d = F(x+2,y-0.5) - F(x+1,y-0.5)
            d+=2*x+3
        else:
            #point outside circle
            #d = F(x+2,y-1.5) - F(x+1,y-0.5)
            d+=2*(x-y)+5
            y-=1
        x+=1
    for i in range(len(pointlist)):
        [x,y]=pointlist[i]
        pointlist.append([y,x])
        pointlist.append([y,-x])
        pointlist.append([x,-y])
        pointlist.append([-x,-y])
        pointlist.append([-y,-x])
        pointlist.append([-y,x])
        pointlist.append([-x,y])
    return pointlist