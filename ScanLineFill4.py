#unfinished
import Boundry

def generatePoints(x, y):
    pointlist = [] #result 
    boundry = Boundry.setBoundry()
    stack = []
    lineFlag = dict.fromkeys(boundry.keys(),0)
    #push seed
    stack.append([x,y])

    #while stack isn't empty
    while (len(stack)!=0):
        seed = stack.pop()

        x,y = seed
        while([x,y] not in boundry):
            pointlist.append[x,y]
            x+=1
        xRight = x-1

        x,y = seed
        while(x not in boundry):
            pointlist.append[x,y]
            x-=1
        xLeft = x+1

        #check the above scanline
        x = xLeft
        y+=1
        while(x<=xRight):
            x


