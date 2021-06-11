"""
|1001|1000|1010|
|0001|0000|0010|
|0101|0100|0110|

LEFT 0001B 1D
RIGHT 0010B 2D
BOTTOM 0100B 4D
TOP 1000B 8D
"""
import LineDda
import LineBresenham

def encode(x, y, XL, YB, XR, YT):
    c = 0
    if(x < XL):
        c |= 1
    if(x > XR):
        c |= 2
    if(y < YB):
        c |= 4
    if(y > YT):
        c |= 8
    return c

def generatePoints(XL, YB, XR, YT, x1, y1, x2, y2,points):
    pointlist = points
    code1 = encode(x1, y1, XL, YB, XR, YT)
    code2 = encode(x2, y2, XL, YB, XR, YT)
    code = 0

    while ((code1 != 0) or (code2 != 0)):     #at least one point is outside

        #At the same side
        if(code1 & code2 != 0):
            return pointlist

        if(code1 != 0):
            code = code1
        else:
            code = code2
        if(code & 1 != 0):
            x = XL
            y = y1+(y2-y1)*(XL-x1)/(x2-x1)
        elif(code & 2 != 0):
            x = XR
            y = y1+(y2-y1)*(XR-x1)/(x2-x1)
        elif(code & 4 != 0):
            y = YB
            x = x1+(x2-x1)*(YB-y1)/(y2-y1)
        elif(code & 8 != 0):
            y = YT
            x = x1+(x2-x1)*(YT-y1)/(y2-y1)

        if(code == code1):
            x1 = x
            y1 = y
            code1 = encode(x, y, XL, YB, XR, YT)
        else:
            x2 = x
            y2 = y
            code2 = encode(x, y, XL, YB, XR, YT)
    
    # pointlist = LineBresenham.generatePoints(x1, y1, x2, y2)

    #delete the points outside boundry
    [x,y]=pointlist[0]
    if(x1!=x2 and y1!=y2):
        while(x !=x1 and y!=y1):
            pointlist.pop(0)
            [x,y]=pointlist[0]
        [x,y] = pointlist[len(pointlist)-1]
        while(x!=x2 and y!=y2):
            pointlist.pop()
            [x,y] = pointlist[len(pointlist)-1]
    elif x1==x2:
        while(y!=y1):
            pointlist.pop(0)
            [x,y]=pointlist[0]
        [x,y] = pointlist[len(pointlist)-1]
        while(y!=y2):
            pointlist.pop()
            [x,y] = pointlist[len(pointlist)-1]        
    elif y1==y2:   
        while(x!=x1):
            pointlist.pop(0)
            [x,y]=pointlist[0]
        [x,y] = pointlist[len(pointlist)-1]
        while(x!=x2):
            pointlist.pop()
            [x,y] = pointlist[len(pointlist)-1]  

    #delete the points on the boundry
    [x,y]=pointlist[0]
    flag = 0
    if x==XL or x==XR or y== YB or y== YT:
        flag = 1
    while(flag!=0):
        pointlist.pop(0)
        [x,y]=pointlist[0]
        if x==XL or x==XR or y== YB or y== YT:
            flag = 1
        else: flag = 0
    [x,y] = pointlist[len(pointlist)-1]
    flag = 0 
    if x==XL or x==XR or y== YB or y== YT:
        flag = 1
    while(flag!=0):
        pointlist.pop()
        [x,y] = pointlist[len(pointlist)-1]
        if x==XL or x==XR or y== YB or y== YT:
            flag = 1
        else: flag = 0

    return pointlist


# print(generatePoints(10, 10, 50, 50, 5, 20, 60, 20))
