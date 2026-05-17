from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtCore import QTimer


class FakeScanner(QWidget):
    def __init__(self):
        super().__init__()

        self.pos_y = 0

        self.timer = QTimer()
        self.timer.timeout.connect(self.animate)
        self.timer.start(16)

    def animate(self):
        self.pos_y += 5

        if self.pos_y > self.height():
            self.pos_y = 0

        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)

        painter.fillRect(
            0,
            self.pos_y,
            self.width(),
            8,
            QColor(255, 0, 255, 120)
        )