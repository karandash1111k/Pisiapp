from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QProgressBar
)
from PyQt6.QtCore import QTimer

from glow_button import GlowButton


class PaymentScreen(QWidget):
    def __init__(self, callback):
        super().__init__()

        self.callback = callback
        self.progress_value = 0

        self.layout = QVBoxLayout(self)

        self.title = QLabel("АКТИВАЦИЯ МАТОЧНОГО ПОТОКА")
        self.title.setObjectName("title")

        self.price = QLabel("250 ₽")
        self.price.setObjectName("price")

        self.status = QLabel("Готово к синхронизации")

        self.progress = QProgressBar()

        self.button = GlowButton("Активировать маточный поток")
        self.button.clicked.connect(self.start_activation)

        self.layout.addStretch()
        self.layout.addWidget(self.title)
        self.layout.addWidget(self.price)
        self.layout.addWidget(self.status)
        self.layout.addWidget(self.progress)
        self.layout.addWidget(self.button)
        self.layout.addStretch()

        self.timer = QTimer()
        self.timer.timeout.connect(self.fake_loading)

    def start_activation(self):
        self.progress_value = 0
        self.timer.start(80)

    def fake_loading(self):
        self.progress_value += 5
        self.progress.setValue(self.progress_value)

        messages = [
            "Сканирование ауры...",
            "Проверка вибраций луны...",
            "Синхронизация с денежным эгрегором..."
        ]

        self.status.setText(messages[(self.progress_value // 30) % 3])

        if self.progress_value >= 100:
            self.timer.stop()
            self.status.setText(
                "Оплата успешно принята высшими силами"
            )

            QTimer.singleShot(1500, self.callback)