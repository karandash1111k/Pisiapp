from PyQt6.QtWidgets import QLabel
from PyQt6.QtGui import QPixmap, QTransform
from PyQt6.QtCore import QTimer


class MoonWidget(QLabel):
    def __init__(self):
        super().__init__()

        self.pixmap_original = QPixmap("assets/moon.png")

        self.angle = 0

        self.timer = QTimer()
        self.timer.timeout.connect(self.rotate_moon)
        self.timer.start(40)

    def rotate_moon(self):
        self.angle += 2

        transform = QTransform().rotate(self.angle)

        rotated = self.pixmap_original.transformed(transform)

        self.setPixmap(rotated)