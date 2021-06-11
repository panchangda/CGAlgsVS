import sys
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPainter, QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget
from PyQt5 import QtGui, QtWidgets
from PyQt5.Qt import QBrush, QHBoxLayout, QIcon, QLabel, QVBoxLayout
from PaintWnd import PaintWindow
import DialogWnds


class GUI(QMainWindow):
    def __init__(self):
        super(GUI, self).__init__()
        self.initUI()
        self.dialogLineDda = DialogWnds.Line()
        self.dialogLineBresenham = DialogWnds.Line()
        self.dialogCircleBrensenham = DialogWnds.Circle()
        self.dialogCircleMidPoint = DialogWnds.Circle()
        self.dialogEllipseMidPoint = DialogWnds.Ellipse()
        self.dialogBoundryFill = DialogWnds.AreaFill()
        self.dialogLineCutting = DialogWnds.LineCutting()

        self.dialogLineDda.dialog_signal.connect(self.paintWindow.drawLineDda)
        self.dialogLineBresenham.dialog_signal.connect(self.paintWindow.drawLineBresenham)
        self.dialogCircleBrensenham.dialog_signal.connect(self.paintWindow.drawCircleBresenham)
        self.dialogCircleMidPoint.dialog_signal.connect(self.paintWindow.drawCircleMidPoint)
        self.dialogEllipseMidPoint.dialog_signal.connect(self.paintWindow.drawEllipseMidPoint)
        self.dialogBoundryFill.dialog_signal.connect(self.paintWindow.drawBoundryFill)
        self.dialogLineCutting.dialog_signal.connect(self.paintWindow.drawLineCutting)

        self.btn1.clicked.connect(self.buttonLineDdaClicked)
        self.btn2.clicked.connect(self.buttonLineBresenhamClicked)
        self.btn4.clicked.connect(self.buttonCircleBresenhamClicked)
        self.btn5.clicked.connect(self.buttonCircleMidPointClicked)
        self.btn6.clicked.connect(self.buttonEllipseMidPointClicked)
        self.btn7.clicked.connect(self.buttonBoundryFillClicked)
        self.btn8.clicked.connect(self.paintWindow.drawBoundry)
        self.btn9.clicked.connect(self.buttonLineCuttingClicked)
        self.btn10.clicked.connect(self.paintWindow.drawEdgeMarkFill)

    def initUI(self):
        self.setWindowTitle('CG Algorithms GUI')
        self.setWindowIcon(QIcon('icon.png'))
        desktop = QtWidgets.QApplication.desktop()
        self.screenWidth = desktop.width()
        self.screenHeight = desktop.height()
        self.resize(self.screenWidth, self.screenHeight)

        self.paintWindow = PaintWindow(int(self.screenWidth/2))

        self.label1 = QLabel("Line")
        self.label2 = QLabel("Circle")
        self.label3 = QLabel("Ellipse")
        self.label4 = QLabel('RIGHTCLICK TO CLEAR THE CANVAS')
        self.label5 = QLabel('Created by PCD')
        self.label6 = QLabel("AreaFill")
        self.label7 = QLabel("LineCutting")
        self.label1.setAlignment(Qt.AlignCenter)
        self.label2.setAlignment(Qt.AlignCenter)
        self.label3.setAlignment(Qt.AlignCenter)
        self.label4.setAlignment(Qt.AlignCenter)
        self.label6.setAlignment(Qt.AlignCenter)
        self.label7.setAlignment(Qt.AlignCenter)
        self.label5.setAlignment(Qt.AlignRight)
        self.btn1 = QPushButton('line-dda')
        self.btn2 = QPushButton('line-bresenham')
        self.btn3 = QPushButton('line-mid-point')
        self.btn4 = QPushButton('circle-brensenham')
        self.btn5 = QPushButton('circle-mid-point')
        self.btn6 = QPushButton('ellipse-mid-point')
        self.btn7 = QPushButton('boundry-Fill-4')
        self.btn10 = QPushButton('EdgeMarkFill')
        self.btn8 = QPushButton('show-boundry')
        self.btn9 = QPushButton('line-cutting-cohen-sutherland')

        

        self.hLayout = QHBoxLayout()
        self.vLayout = QVBoxLayout()
        self.vLayout.addWidget(self.label4)
        self.vLayout.addWidget(self.label1)
        self.vLayout.addWidget(self.btn1)
        self.vLayout.addWidget(self.btn2)
        self.vLayout.addWidget(self.btn3)
        self.vLayout.addWidget(self.label2)
        self.vLayout.addWidget(self.btn4)
        self.vLayout.addWidget(self.btn5)
        self.vLayout.addWidget(self.label3)
        self.vLayout.addWidget(self.btn6)
        self.vLayout.addWidget(self.label6)
        self.vLayout.addWidget(self.btn8)
        self.vLayout.addWidget(self.btn7)
        self.vLayout.addWidget(self.btn10)
        self.vLayout.addWidget(self.label7)
        self.vLayout.addWidget(self.btn9)
        
        self.vLayout.addWidget(self.label5)

        self.vwg = QtWidgets.QWidget()
        self.vwg.setLayout(self.vLayout)
        self.hLayout.addWidget(self.paintWindow)
        self.hLayout.addWidget(self.vwg)
        self.wid = QWidget(self)
        self.setCentralWidget(self.wid)
        self.wid.setLayout(self.hLayout)
        # self.paintWindow.show()

    def buttonLineDdaClicked(self):
        self.dialogLineDda.show()

    def buttonLineBresenhamClicked(self):
        self.dialogLineBresenham.show()

    def buttonCircleBresenhamClicked(self):
        self.dialogCircleBrensenham.show()
    
    def buttonCircleMidPointClicked(self):
        self.dialogCircleMidPoint.show()
        
    def buttonEllipseMidPointClicked(self):
        self.dialogEllipseMidPoint.show()
    
    def buttonBoundryFillClicked(self):
        self.dialogBoundryFill.show()
    
    def buttonLineCuttingClicked(self):
        self.dialogLineCutting.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    instance = GUI()
    instance.show()
    sys.exit(app.exec_())
