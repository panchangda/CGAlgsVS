import sys
import time
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import *
from PyQt5.Qt import QPixmap
import LineDda
import LineBresenham
import CircleBresenham
import CircleMidPoint
from PyQt5 import QtTest
import EllipseMidPoint
import BoundryFill4
import Boundry
from DialogWnds import LineCutting
import LineCuttingCohenSutherland
import EdgeMarkFill


class PaintWindow(QWidget):
    def __init__(self, width):
        super(PaintWindow, self).__init__()
        self.resize(width, width)
        self.width = width
        self.pen = QPen(Qt.SolidLine)
        self.pen1 = QPen(Qt.SolidLine)
        self.pen1.setWidth(4)
        self.penPoint = QPen(Qt.black, 5)
        self.penRed = QPen(Qt.red,5)
        self.penBlue = QPen(Qt.blue,5)
        self.penYellow = QPen(Qt.yellow,5)

        self.pixMap = QPixmap(width, width)
        self.pixMap.fill(Qt.white)

        self.flag = 0

        self.x = 0
        self.y = 0

        self.pointlist = []
        for i in range(10):
            [x, y] = [i, i]
            self.pointlist.append([x, y])
        # self.pen2.setColor(Qt.red)

    def paintEvent(self, QPaintEvent):

        # initialize two painters for pixmap&window it self
        painterPixMap = QPainter(self.pixMap)
        painterSelf = QPainter(self)

        """
        when flag == 0
        draw the coordinate sys
        when flag == 1
        draw the point(black)
        when flag == 2
        draw the point(blue)
        when flag == 3
        draw the point(red)
        """

        if self.flag == 0:
            painterPixMap.setPen(self.pen)
            for i in range(0, self.width, 10):
                painterPixMap.drawLine(0, i, self.width, i)
                painterPixMap.drawLine(i, 0, i, self.width)
            painterPixMap.setPen(self.pen1)
            painterPixMap.drawLine(0, self.width/2, self.width, self.width/2)
            painterPixMap.drawLine(self.width/2, 0, self.width/2, self.width)
            painterSelf.drawPixmap(0, 0, self.pixMap)

        elif self.flag == 1:
            painterPixMap.setPen(self.penPoint)
            painterPixMap.drawPoint(self.x, self.y)
            painterSelf.drawPixmap(0, 0, self.pixMap)

        elif self.flag == 2:
            painterPixMap.setPen(self.penBlue)
            painterPixMap.drawPoint(self.x, self.y)
            painterSelf.drawPixmap(0, 0, self.pixMap)
        
        elif self.flag == 3:
            painterPixMap.setPen(self.penRed)
            painterPixMap.drawPoint(self.x, self.y)
            painterSelf.drawPixmap(0, 0, self.pixMap)

    # #draw without pause
    # def drawImediately(self,pointlist):
    #     self.flag = 1
    #     for i in range(len(pointlist)):
    #         [x, y] = pointlist[i]
    #         self.x = int(x*10 + self.width/2)
    #         self.y = int(self.width/2 - y*10)
    #         self.update()

    #draw black points
    def drawBlack(self, pointlist):
        self.flag = 1
        for i in range(len(pointlist)):
            [x, y] = pointlist[i]
            self.x = int(x*10 + self.width/2)
            self.y = int(self.width/2 - y*10)
            self.update()
            QtTest.QTest.qWait(20)   # 1000 mecs pause between drawpoint

    #draw blue points
    def drawBlue(self,pointlist):
        self.flag = 2
        for i in range(len(pointlist)):
            [x, y] = pointlist[i]
            self.x = int(x*10 + self.width/2)
            self.y = int(self.width/2 - y*10)
            self.update()
            QtTest.QTest.qWait(5)   # 1000 mecs pause between drawpoint

    ##draw red points
    def drawRed(self,pointlist):
        self.flag = 3
        for i in range(len(pointlist)):
            [x, y] = pointlist[i]
            self.x = int(x*10 + self.width/2)
            self.y = int(self.width/2 - y*10)
            self.update()
            QtTest.QTest.qWait(7)   # 1000 mecs pause between drawpoint

    def drawLineDda(self, x1, y1, x2, y2):
        pointlist = LineDda.generatePoints(x1, y1, x2, y2)
        self.drawBlack(pointlist)

    def drawLineBresenham(self, x1, y1, x2, y2):
        pointlist = LineBresenham.generatePoints(x1, y1, x2, y2)
        self.drawBlack(pointlist)

    def drawCircleBresenham(self, r):
        pointlist = CircleBresenham.generatePoints(r)
        self.drawBlack(pointlist)

    def drawCircleMidPoint(self, r):
        pointlist = CircleMidPoint.generatePoints(r)
        self.drawBlack(pointlist)

    def drawEllipseMidPoint(self, a, b):
        pointlist = EllipseMidPoint.generatePoints(a, b)
        self.drawBlack(pointlist)

    def drawBoundry(self):
        self.drawBlue(Boundry.setBoundry())

    def drawBoundryFill(self,x,y):
        pointlist = BoundryFill4.generatePoints(x,y)
        self.drawRed(pointlist)
    
    def drawEdgeMarkFill(self):
        self.drawRed(EdgeMarkFill.generatePoints())

    def drawLineCutting(self,XL,YB,XR,YT,x3,y3,x4,y4):
        self.drawBlue(LineDda.generatePoints(XL,YB,XL,YT))
        self.drawBlue(LineDda.generatePoints(XL,YT,XR,YT))
        self.drawBlue(LineDda.generatePoints(XR,YT,XR,YB))
        self.drawBlue(LineDda.generatePoints(XR,YB,XL,YB))
        points = LineDda.generatePoints(x3,y3,x4,y4)
        self.drawBlack(points)
        self.drawRed(LineCuttingCohenSutherland.generatePoints(XL,YB,XR,YT,x3,y3,x4,y4,points))
        
    def mousePressEvent(self, QMouseEvent):
        if QMouseEvent.button() == Qt.RightButton:
            self.pixMap.fill(Qt.white)
            self.flag = 0
            self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    PaintWindow = PaintWindow(800)
    PaintWindow.show()
    sys.exit(app.exec_())
