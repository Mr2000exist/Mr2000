# fist_made prototype

import math
import sys
from PyQt6.QtWidgets import QWidget, QPushButton, QApplication, QLabel, QGridLayout
from PyQt6.QtCore import Qt

resolution_w = 1920
resolution_h = 1080

button_size = math.floor(
    (resolution_w if resolution_w < resolution_h else resolution_h) / 10
)


class BodyControl(QWidget):
    text = "NULL"

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QGridLayout()
        button_forward = QPushButton("↑", self)
        button_forward.clicked.connect(self.moveForward)
        layout.addWidget(button_forward, 0, 1)

        button_backword = QPushButton("↓", self)
        button_backword.clicked.connect(self.moveBackward)
        layout.addWidget(button_backword, 2, 1)

        button_turnleft = QPushButton("←", self)
        button_turnleft.clicked.connect(self.turnLeft)
        layout.addWidget(button_turnleft, 1, 0)

        button_turnright = QPushButton("→", self)
        button_turnright.clicked.connect(self.turnRight)
        layout.addWidget(button_turnright, 1, 2)

        button_kill = QPushButton("X", self)
        button_kill.clicked.connect(QApplication.instance().quit)
        button_kill.setGeometry(
            200, 150, math.floor(button_size * 0.5), math.floor(button_size * 0.5)
        )
        button_kill.move(
            math.floor(resolution_w - button_size * 1), math.floor(button_size * 0.5)
        )

        self.lbl = QLabel(self.text, self)
        layout.addWidget(self.lbl, 1, 1)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.setLayout(layout)
        self.setWindowTitle("Prototype")
        self.showFullScreen()

    def moveForward(self):
        self.lbl.setText("forw")

    def moveBackward(self):
        self.lbl.setText("back")

    def turnLeft(self):
        self.lbl.setText("left")

    def turnRight(self):
        self.lbl.setText("right")


def main():
    app = QApplication(sys.argv)
    app.processEvents()
    BC = BodyControl()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
