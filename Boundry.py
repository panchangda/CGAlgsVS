import LineDda
def setBoundry():
    boundry = []
    line1 = LineDda.generatePoints(5,3,15,60)
    line2 = LineDda.generatePoints(15,60,30,40)
    line3 = LineDda.generatePoints(30,40,55,50)
    line4 = LineDda.generatePoints(55,50,60,10)
    line5 = LineDda.generatePoints(60,10,5,3)
    #inside space
    line6 = LineDda.generatePoints(20,20,20,30)
    line7 = LineDda.generatePoints(20,30,30,30)
    line8 = LineDda.generatePoints(30,30,30,20)
    line9 = LineDda.generatePoints(30,20,20,20)

    boundry = line1+line2+line3+line4+line5+line6+line7+line8+line9
    return boundry
# print(setBoundry())