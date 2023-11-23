#!/bin/python3
# fist_made prototype

import math
import sys
#from robotics import motor_control
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QLabel, QGridLayout, QHBoxLayout, QVBoxLayout, QSlider, QMainWindow, QSizePolicy, QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QColor, QImage, QPixmap, QPainter

resolution_w = 480 
resolution_h = 640

button_size = math.floor(
    (resolution_w if resolution_w < resolution_h else resolution_h) / 10
)

class BodyControl(QWidget):
    #motor_ctrl = motor_control.MotorControl()

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        fileName = './grayscale_bitmap.bmp'

        #layout setting
        v_layout = QVBoxLayout()
        grid_layout = QGridLayout()
        kill_layout = QHBoxLayout()
        kill_layout.addStretch()
        pow_slider_layout = QVBoxLayout()

        pow_slider_layout.setContentsMargins(0,0,0,0)
        
        power_slider = QSlider(Qt.Orientation.Horizontal, self)
        power_slider.setRange(1, 100)

        #grid_layout.addWidget(QColor('red'))

        self.imageLabel = QLabel()
        #self.imageLabel.setBackgroundRole(QPalette.Base)
        #self.imageLabel.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.imageLabel.setScaledContents(True)

        if fileName:
            image = QImage(fileName)
            if image.isNull():
                QMessageBox.information(self, "Image Viewer", "Cannot load %s." % fileName)
                return

            self.imageLabel.setPixmap(QPixmap.fromImage(image))
            self.scaleFactor = 1.0/(self.imageLabel.pixmap().size() * 0.003125)

        self.imageLabel.resize(self.scaleFactor * self.imageLabel.pixmap().size())

            #self.imageLabel.setVisible(True)
            #self.imageLabel.show()
        
        #grid_layout.cellRect(3,3)
        #grid_layout.rowStretch(button_size*3)
        #grid_layout.columnStretch(button_size*3)

        #grid_button_layout
        button_forward = QPushButton("↑", self)
        button_forward.clicked.connect(self.moveForward)
        grid_layout.addWidget(button_forward, 0, 1)

        button_backword = QPushButton("↓", self)
        button_backword.clicked.connect(self.moveBackward)
        grid_layout.addWidget(button_backword, 2, 1)

        button_turnleft = QPushButton("←", self)
        button_turnleft.clicked.connect(self.turnLeft)
        grid_layout.addWidget(button_turnleft, 1, 0)

        button_turnright = QPushButton("→", self)
        button_turnright.clicked.connect(self.turnRight)
        grid_layout.addWidget(button_turnright, 1, 2)

        button_kill = QPushButton("X", self)
        button_kill.clicked.connect(QApplication.instance().quit)
        kill_layout.addWidget(button_kill)

        button_stop = QPushButton("-", self)
        button_stop.clicked.connect(self.stop)
        grid_layout.addWidget(button_stop, 1, 1)
        grid_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        #power_slide_layout
        power_slider.valueChanged.connect(self.slider_changed)
        self.power_status_label = QLabel('1', self)
        pow_slider_layout.addWidget(power_slider)
        pow_slider_layout.addWidget(self.power_status_label)

        kill_layout.setContentsMargins(button_size*9, button_size, math.floor(button_size/2), 0)
        v_layout.addWidget(self.imageLabel)
        v_layout.addLayout(kill_layout)
        v_layout.addLayout(pow_slider_layout)
        v_layout.addLayout(grid_layout)
        self.setLayout(v_layout)
        self.setGeometry(200, 150, resolution_w, resolution_h)
        self.setWindowTitle("Prototype")
        self.show()

    #buttons_actions_funcs
    def moveForward(self):
        self.motor_ctrl.front()

    def moveBackward(self):
        self.motor_ctrl.back()

    def turnLeft(self):
        self.motor_ctrl.left()

    def turnRight(self):
        self.motor_ctrl.right()

    def stop(self):
        self.motor_ctrl.stop()

    def slider_changed(self, p) : 
        self.power_status_label.setText(str(p))


def main():
    app = QApplication(sys.argv)
    app.processEvents()
    BC = BodyControl()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
