from PyQt5.Qt import QGridLayout, QLabel, QLineEdit, QPushButton, Qt, pyqtSignal
from PyQt5.QtWidgets import QDialog

class Line(QDialog):
    dialog_signal=pyqtSignal(int,int,int,int)
    def __init__(self):
        super(Line,self).__init__()
        self.Label_x1 = QLabel('x1') 
        self.Label_y1 = QLabel('y1')  
        self.Label_x2 = QLabel('x2')  
        self.Label_y2 = QLabel('y2')    
        self.LineEdit_x1 = QLineEdit()
        self.LineEdit_y1 = QLineEdit()  
        self.LineEdit_x2 = QLineEdit()  
        self.LineEdit_y2 = QLineEdit()   
        self.confirm_button = QPushButton("Confirm") 
        self.grid = QGridLayout()  
        self.grid.setSpacing(10)  
        self.grid.addWidget(self.Label_x1, 1, 0)  
        self.grid.addWidget(self.LineEdit_x1, 1, 1)
        self.grid.addWidget(self.Label_y1, 2, 0)  
        self.grid.addWidget(self.LineEdit_y1, 2, 1)
        self.grid.addWidget(self.Label_x2, 3, 0)  
        self.grid.addWidget(self.LineEdit_x2, 3, 1)
        self.grid.addWidget(self.Label_y2, 4, 0)  
        self.grid.addWidget(self.LineEdit_y2, 4, 1)  
        self.grid.addWidget(self.confirm_button,5,0,1,2)
        self.setLayout(self.grid)   
        self.setGeometry(200,700, 600, 300)  
        self.setWindowTitle('Setup Parameters')
        self.confirm_button.clicked.connect(self.slot)

    def slot(self):
        x1 = int(self.LineEdit_x1.text())
        y1 = int(self.LineEdit_y1.text())
        x2 = int(self.LineEdit_x2.text())
        y2 = int(self.LineEdit_y2.text())
        
        # self.hide()
        self.close()
        #发送信号
        self.dialog_signal.emit(x1,y1,x2,y2)

        #清空
        self.LineEdit_x1.setText("")
        self.LineEdit_y1.setText("")
        self.LineEdit_x2.setText("")
        self.LineEdit_y2.setText("")

class Circle(QDialog):
    dialog_signal=pyqtSignal(int)
    def __init__(self):
        super(Circle,self).__init__()
        self.Label_x = QLabel('center x') 
        self.Label_y = QLabel('center y')  
        self.Label_r = QLabel('r')     
        self.LineEdit_x = QLineEdit()
        self.LineEdit_y = QLineEdit()  
        self.LineEdit_r = QLineEdit()   
        self.LineEdit_x.setText("0")
        self.LineEdit_y.setText("0")
        self.confirm_button = QPushButton("Confirm") 
        self.grid = QGridLayout()  
        self.grid.setSpacing(10)  
        self.grid.addWidget(self.Label_x, 1, 0)  
        self.grid.addWidget(self.LineEdit_x, 1, 1)
        self.grid.addWidget(self.Label_y, 2, 0)  
        self.grid.addWidget(self.LineEdit_y, 2, 1)
        self.grid.addWidget(self.Label_r, 3, 0)  
        self.grid.addWidget(self.LineEdit_r, 3, 1)
        self.grid.addWidget(self.confirm_button,4,0,1,2)
        self.setLayout(self.grid)   
        self.setGeometry(200,700, 600, 300)  
        self.setWindowTitle('Setup Parameters')
        self.confirm_button.clicked.connect(self.slot)

    def slot(self):
        x = int(self.LineEdit_x.text())
        y = int(self.LineEdit_y.text())
        r = int(self.LineEdit_r.text())

        # self.hide()
        self.close()
        #发送信号
        self.dialog_signal.emit(r)

        #清空
        self.LineEdit_x.setText("0")
        self.LineEdit_y.setText("0")
        self.LineEdit_r.setText("")

class Ellipse(QDialog):
    dialog_signal=pyqtSignal(int,int)
    def __init__(self):
        super(Ellipse,self).__init__()
        self.Label_Fx = QLabel('F(x) = b^2*x^2+a^2*y^2-a^2*b^2') 
        self.Label_a = QLabel('a') 
        self.Label_b = QLabel('b')  
            
        self.LineEdit_b = QLineEdit()  
        self.LineEdit_a = QLineEdit()   

        self.confirm_button = QPushButton("Confirm") 
        self.grid = QGridLayout()  
        self.grid.setSpacing(10)  
        self.grid.addWidget(self.Label_Fx, 1, 0,1,2)  
        self.grid.addWidget(self.Label_a, 2, 0)  
        self.grid.addWidget(self.LineEdit_a, 2, 1)
        self.grid.addWidget(self.Label_b, 3, 0)  
        self.grid.addWidget(self.LineEdit_b, 3, 1)
        self.grid.addWidget(self.confirm_button,4,0,1,2)
        self.setLayout(self.grid)   
        self.setGeometry(200,700, 600, 300)  
        self.setWindowTitle('Setup Parameters')
        self.confirm_button.clicked.connect(self.slot)

    def slot(self):
        a = int(self.LineEdit_a.text())
        b = int(self.LineEdit_b.text())
       

        # self.hide()
        self.close()
        #发送信号
        self.dialog_signal.emit(a,b)

        #清空
        self.LineEdit_a.setText("")
        self.LineEdit_b.setText("")
        
class AreaFill(QDialog):
    dialog_signal=pyqtSignal(int,int)
    def __init__(self):
        super(AreaFill,self).__init__()
        self.Label_x = QLabel('x') 
        self.Label_y = QLabel('y')  
            
        self.LineEdit_x = QLineEdit()  
        self.LineEdit_y = QLineEdit()   

        self.confirm_button = QPushButton("Confirm") 
        self.grid = QGridLayout()  
        self.grid.setSpacing(10)  
        self.grid.addWidget(self.Label_x, 1, 0)  
        self.grid.addWidget(self.LineEdit_x, 1, 1)  
        self.grid.addWidget(self.Label_y, 2, 0)
        self.grid.addWidget(self.LineEdit_y, 2, 1)
        self.grid.addWidget(self.confirm_button,3,0,1,2)
        self.setLayout(self.grid)   
        self.setGeometry(200,700, 600, 300)  
        self.setWindowTitle('Setup Parameters')
        self.confirm_button.clicked.connect(self.slot)

    def slot(self):
        x = int(self.LineEdit_x.text())
        y = int(self.LineEdit_y.text())
       

        # self.hide()
        self.close()
        #发送信号
        self.dialog_signal.emit(x,y)

        #清空
        self.LineEdit_x.setText("")
        self.LineEdit_y.setText("")

class LineCutting(QDialog):
    dialog_signal=pyqtSignal(int,int,int,int,int,int,int,int)
    def __init__(self):
        super(LineCutting,self).__init__()
        self.Label_x1 = QLabel('WindowCoordinate leftbottom x1') 
        self.Label_y1 = QLabel('WindowCoordinate leftbottom y1')
        self.Label_x2 = QLabel('WindowCoordinate righttop x2') 
        self.Label_y2 = QLabel('WindowCoordinate righttop y2') 
        self.Label_x3 = QLabel('line start x3') 
        self.Label_y3 = QLabel('line start y3') 
        self.Label_x4 = QLabel('line end x4') 
        self.Label_y4 = QLabel('line end y4') 
            
        self.LineEdit_x1 = QLineEdit()  
        self.LineEdit_y1 = QLineEdit()  
        self.LineEdit_x2 = QLineEdit()  
        self.LineEdit_y2 = QLineEdit() 
        self.LineEdit_x3 = QLineEdit()  
        self.LineEdit_y3 = QLineEdit() 
        self.LineEdit_x4 = QLineEdit()  
        self.LineEdit_y4 = QLineEdit()  

        self.confirm_button = QPushButton("Confirm") 
        self.grid = QGridLayout()  
        self.grid.setSpacing(10)  
        self.grid.addWidget(self.Label_x1, 1, 0)  
        self.grid.addWidget(self.LineEdit_x1, 1, 1)  
        self.grid.addWidget(self.Label_y1, 2, 0)
        self.grid.addWidget(self.LineEdit_y1, 2, 1)
        self.grid.addWidget(self.Label_x2, 3, 0)  
        self.grid.addWidget(self.LineEdit_x2, 3, 1)  
        self.grid.addWidget(self.Label_y2, 4, 0)
        self.grid.addWidget(self.LineEdit_y2, 4, 1)
        self.grid.addWidget(self.Label_x3, 5, 0)  
        self.grid.addWidget(self.LineEdit_x3, 5, 1)  
        self.grid.addWidget(self.Label_y3, 6, 0)
        self.grid.addWidget(self.LineEdit_y3, 6, 1)
        self.grid.addWidget(self.Label_x4, 7, 0)  
        self.grid.addWidget(self.LineEdit_x4, 7, 1)  
        self.grid.addWidget(self.Label_y4, 8, 0)
        self.grid.addWidget(self.LineEdit_y4, 8, 1)
        self.grid.addWidget(self.confirm_button,9,0,1,2)
        self.setLayout(self.grid)   
        self.setGeometry(200,700, 600, 300)  
        self.setWindowTitle('Setup Parameters')
        self.confirm_button.clicked.connect(self.slot)

    def slot(self):
        x1 = int(self.LineEdit_x1.text())
        y1 = int(self.LineEdit_y1.text())
        x2 = int(self.LineEdit_x2.text())
        y2 = int(self.LineEdit_y2.text())
        x3 = int(self.LineEdit_x3.text())
        y3 = int(self.LineEdit_y3.text())
        x4 = int(self.LineEdit_x4.text())
        y4 = int(self.LineEdit_y4.text())
       

        # self.hide()
        self.close()
        #发送信号
        self.dialog_signal.emit(x1,y1,x2,y2,x3,y3,x4,y4)

        #清空
        # self.LineEdit_x1.setText("")
        # self.LineEdit_y1.setText("")
        # self.LineEdit_x2.setText("")
        # self.LineEdit_y2.setText("")
        self.LineEdit_x3.setText("")
        self.LineEdit_y3.setText("")
        self.LineEdit_x4.setText("")
        self.LineEdit_y4.setText("")

