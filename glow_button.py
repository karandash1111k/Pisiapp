from PyQt6.QtWidgets import QPushButton, QGraphicsDropShadowEffect
from PyQt6.QtGui import QColor
from PyQt6.QtCore import QPropertyAnimation


class GlowButton(QPushButton):
    def __init__(self, text: str):
        super().__init__(text)

        glow = QGraphicsDropShadowEffect(self)
        glow.setBlurRadius(30)
        glow.setColor(QColor("#ff00ff"))
        glow.setOffset(0)

        self.setGraphicsEffect(glow)

        self.anim = QPropertyAnimation(glow, b"blurRadius")
        self.anim.setDuration(700)
        self.anim.setStartValue(15)
        self.anim.setEndValue(45)

    def enterEvent(self, event):
        self.anim.start()
        super().enterEvent(event)