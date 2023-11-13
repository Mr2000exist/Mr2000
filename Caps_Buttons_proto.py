#fist_made prototype

import math
import sys
from PyQt6.QtWidgets import QWidget, QPushButton, QApplication, QLabel

resolution_w = 1920
resolution_h = 1080

button_size = math.floor((resolution_w if resolution_w < resolution_h else resolution_h) / 10)


class Body_Control(QWidget) : 
    text = 'NULL'
    def __init__(self) : 
        super().__init__()

        self.initUI()

    def initUI(self) : 

        button_forward = QPushButton('^\n|', self)
        button_forward.clicked.connect(self.moveForward)
        button_forward.setGeometry(200, 150, button_size, button_size)
        button_forward.move(resolution_w-button_size*3, math.floor(resolution_h-button_size*4.5))

        button_backword = QPushButton('!', self)
        button_backword.clicked.connect(self.moveBackword)
        button_backword.setGeometry(200, 150, button_size, button_size)
        button_backword.move(resolution_w-button_size*3, math.floor(resolution_h-button_size*1.5))

        button_turnleft = QPushButton('<-', self)
        button_turnleft.clicked.connect(self.turnLeft)
        button_turnleft.setGeometry(200, 150, button_size, button_size)
        button_turnleft.move(math.floor(resolution_w-button_size*4.5), resolution_h-button_size*3)
        
        button_turnright = QPushButton('->', self)
        button_turnright.clicked.connect(self.turnRight)
        button_turnright.setGeometry(200, 150, button_size, button_size)
        button_turnright.move(math.floor(resolution_w-button_size*1.5), resolution_h-button_size*3)

        button_kill = QPushButton('X', self)
        button_kill.clicked.connect(QApplication.instance().quit)
        button_kill.setGeometry(200, 150, math.floor(button_size*0.5), math.floor(button_size*0.5))
        button_kill.move(math.floor(resolution_w-button_size*1), math.floor(button_size*0.5))

        self.lbl = QLabel(self.text, self)
        self.lbl.move(math.floor(resolution_w/2), math.floor(resolution_h/2))

        self.setGeometry(200, 150, resolution_w, resolution_h)
        self.setWindowTitle('Prototype')
        self.showFullScreen()

    def moveForward(self) : 
        self.lbl.setText('forw')

    def moveBackword(self) : 
        self.lbl.setText('back')
    def turnLeft(self) : 
        self.lbl.setText('left')
    def turnRight(self) : 
        self.lbl.setText('right')


def main() :  
    app = QApplication(sys.argv)
    app.processEvents()
    BC = Body_Control()
    sys.exit(app.exec())

if __name__ == '__main__' : 
    main()
