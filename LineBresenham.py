
# #改进版Bresenham算法实现
# def generatePoints(x1,y1,x2,y2):
#     pointlist = []
#     dx = x2 -x1
#     dy = y2 -y1
#     x = x1
#     y = y1
#     e = -dx
#     for i in range(dx):
#         pointlist.append([x,y])
#         x+=1
#         e+=2*dy
#         if e >= 0:
#             y+=1
#             e-=2*dx
        
#     return pointlist

#原始版Bresenham算法实现
def generatePoints(x1,y1,x2,y2):
    pointlist = []
    dx = x2-x1
    dy = y2-y1
    e = -0.5
    x = x1
    y = y1

    if(dx>0):
        increx = 1
    elif(dx<0):
        increx = -1
    else:
        increx = 0
    if(dy>0):
        increy = 1
    elif(dy<0):
        increy = -1
    else:
        increy = 0
        
    #special case
    if dx==0 :
        k=1
        for i in range(abs(dy)+1):
            pointlist.append([x,y])
            x+=increx
            e+=k
            if e>=0:
                y+=increy
                e-=1
    elif(abs(dy/dx)<=1):
        k = abs(dy/dx)
        #special case 
        if(dy==0):
            k=1
        for i in range(abs(dx)+1):
            #drawpixel(x,y)
            pointlist.append([x,y])
            x+=increx
            e+=k
            if e>=0:
                y+=increy
                e-=1
    else:
        k = abs(dx/dy)
        x,y = y,x
        increx,increy=increy,increx
        for i in range(abs(dy)+1):
            #drawpixel(x,y)
            pointlist.append([y,x])
            x+=increx
            e+=k
            if e>=0:
                y+=increy
                e-=1
    
    return pointlist
        
# p = generatePoints(0,0,-2,5)
# for i in range(len(p)):
#     print(p[i])