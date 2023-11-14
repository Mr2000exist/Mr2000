#!/bin/python3
# fist_made prototype

import math
import sys
#from robotics import motor_control
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QLabel, QGridLayout, QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import Qt

resolution_w = 640 
resolution_h = 480

button_size = math.floor(
    (resolution_w if resolution_w < resolution_h else resolution_h) / 10
)


class BodyControl(QWidget):
    text = "NULL"
    motor_ctrl = motor_control.MotorControl()

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        v_layout = QVBoxLayout()
        grid_layout = QGridLayout()
        h_layout = QHBoxLayout()
        h_layout.addStretch()

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
        h_layout.addWidget(button_kill)

        button_stop = QPushButton("-", self)
        button_stop.clicked.connect(self.stop)
        layout.addWidget(button_stop, 1, 1)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        h_layout.setContentsMargins(button_size*9, button_size, math.floor(button_size/2), 0)
        v_layout.addLayout(h_layout)
        v_layout.addLayout(grid_layout)
        self.setLayout(v_layout)
        self.setGeometry(200, 150, resolution_w, resolution_h)
        self.setWindowTitle("Prototype")
        self.show()

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


def main():
    app = QApplication(sys.argv)
    app.processEvents()
    BC = BodyControl()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
