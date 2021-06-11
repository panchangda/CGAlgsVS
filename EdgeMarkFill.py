#unfinished
import Boundry

def generatePoints():
    pointlist = []
    boundry = Boundry.setBoundry()
    [x, y] = boundry[0]
    yMin=y
    yMax = y
    xMin=x
    xMax = x
    #traverse boundry points to get the range of x&y
    for i in range(len(boundry)):
        [x, y] = boundry[i]
        if(y > yMax):
            yMax = y
        elif(y < yMin):
            yMin = y
        if(x > xMax):
            xMax = x
        elif(x < xMin):
            xMin = x

    for y in range(yMin+1, yMax):
        inside = False
        tempPoints = []
        #if the boundry is continuing, inside remains the same
        for x in range(xMin,xMax+1):
            if(inside):
                if ((([x,y] in boundry) and ([x+1,y] not in boundry))
                or(([x,y] in boundry) and ([x-1,y] not in boundry))):
                    inside = ~inside
                    #检测到boundry才将前一段添加至pointlist
                    if(inside==False):
                        pointlist += tempPoints
                        tempPoints = []
                    continue

            else:
                if(([x,y] in boundry) and ([x+1,y] not in boundry)):
                    inside = ~inside
                    continue

            if(inside):
                tempPoints.append([x, y])

    return pointlist
