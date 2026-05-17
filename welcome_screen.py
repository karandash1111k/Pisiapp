from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel
)

from glow_button import GlowButton


class WelcomeScreen(QWidget):
    def __init__(self, callback):
        super().__init__()

        layout = QVBoxLayout(self)

        title = QLabel("Открой Маточный Поток Сознания")
        title.setObjectName("title")

        subtitle = QLabel(
            "Соедини денежный канал с вибрациями вселенной"
        )
        subtitle.setObjectName("subtitle")


        button = GlowButton("ВОЙТИ В КОСМИЧЕСКИЙ ПОТОК")
        button.clicked.connect(callback)

        layout.addStretch()
        layout.addWidget(title)
        layout.addWidget(subtitle)
        layout.addSpacing(30)
        layout.addWidget(button)
        layout.addSpacing(30)
        layout.addStretch()