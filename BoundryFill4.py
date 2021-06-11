import Boundry
def generatePoints(x,y):
    pointlist = []
    boundry = Boundry.setBoundry()
    pointsAlreadyDrawed = []
    stack = []
    stack.append([x,y])
    while(len(stack)!=0):
        [x,y]=stack.pop()
        if(([x,y] not in boundry) and 
        ([x,y] not in pointsAlreadyDrawed)):
            pointlist.append([x,y])#drawpixel
            pointsAlreadyDrawed.append([x,y])
            stack.append([x-1,y])
            stack.append([x+1,y])
            stack.append([x,y-1])
            stack.append([x,y+1])
    return pointlist
        
