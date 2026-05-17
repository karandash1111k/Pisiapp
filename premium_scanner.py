import random

from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QMessageBox,
    QProgressBar,
    QFrame,
    QHBoxLayout
)

from PyQt6.QtCore import QTimer
from PyQt6.QtGui import QColor

from glow_button import GlowButton


RESULTS = [
    "Карма совместима с луной на 73%",
    "Маточное облако перегружено",
    "Обнаружен ретроградный кэш",
    "Лунный AI рекомендует купить ещё один курс",
    "Аура синхронизирована с NFT-вселенной",
    "Чакра денег ушла в timeout",
    "Обнаружен дефицит premium-вибраций",
]


TARIFFS = [
    ("Womb Basic", "400 ₽"),
    ("Goddess PRO", "1490 ₽"),
    ("Lunar Oracle MAX", "9990 ₽"),
    ("Quantum Empress ELITE", "77777 ₽"),
]


class PremiumScanner(QWidget):

    def __init__(self):
        super().__init__()

        self.paid = False
        self.value = 0
        self.clicks = 0

        layout = QVBoxLayout(self)

        self.title = QLabel(
            "DeepWomb™ AI Scanner PRO"
        )
        self.title.setObjectName("title")

        self.status = QLabel(
            "AI Scanner OFFLINE"
        )

        self.subscription = QLabel(
            "🌙 PREMIUM INACTIVE"
        )

        self.subscription.setObjectName(
            "subscriptionLabel"
        )

        self.progress = QProgressBar()

        self.scan_button = GlowButton(
            "Запустить AI-анализ кармы"
        )

        self.scan_button.clicked.connect(
            self.handle_scan
        )

        layout.addWidget(self.title)
        layout.addWidget(self.status)
        layout.addWidget(self.subscription)
        layout.addWidget(self.progress)

        layout.addSpacing(20)

        tariff_title = QLabel(
            "КВАНТОВЫЕ ТАРИФЫ"
        )
        tariff_title.setObjectName("subtitle")

        layout.addWidget(tariff_title)

        for name, price in TARIFFS:

            card = self.make_tariff_card(
                name,
                price
            )

            layout.addWidget(card)

        layout.addSpacing(20)

        self.metrics = QLabel(
            "Moon Ping: 4ms\n"
            "Quantum Uptime: 99.9%\n"
            "Aura GPU: RTX 5090 Ti\n"
            "Rendering womb consciousness..."
        )

        self.metrics.setObjectName("metrics")

        layout.addWidget(self.metrics)

        layout.addSpacing(20)

        layout.addWidget(self.scan_button)

        self.timer = QTimer()
        self.timer.timeout.connect(
            self.fake_scan
        )

    def make_tariff_card(
        self,
        name: str,
        price: str
    ) -> QFrame:

        frame = QFrame()
        frame.setObjectName("tariffCard")

        l = QHBoxLayout(frame)

        title = QLabel(name)
        title.setObjectName("tariffTitle")

        cost = QLabel(price)
        cost.setObjectName("tariffPrice")

        l.addWidget(title)
        l.addStretch()
        l.addWidget(cost)

        return frame

    def handle_scan(self):

        self.clicks += 1

        if self.clicks > 10:

            self.status.setText(
                "⚠ Обнаружен взлом ауры"
            )

            return

        if not self.paid:
            self.show_paywall()
            return

        self.start_scan()

    def show_paywall(self):

        msg = QMessageBox(self)

        msg.setWindowTitle(
            "Premium Upgrade Required"
        )

        msg.setText(
            "⚠ Функция доступна только\n"
            "в тарифе DEEP WOMB PREMIUM AI+\n\n"
            "Стоимость:\n"
            "400 ₽"
        )

        buy_btn = msg.addButton(
            "Разблокировать через квантовую оплату",
            QMessageBox.ButtonRole.AcceptRole
        )

        msg.addButton(
            "Позже синхронизировать ауру",
            QMessageBox.ButtonRole.RejectRole
        )

        msg.exec()

        if msg.clickedButton() == buy_btn:
            self.activate_premium()

    def activate_premium(self):

        self.status.setText(
            "Подключение к lunar blockchain..."
        )

        QTimer.singleShot(
            1000,
            lambda: self.status.setText(
                "Проверка NFT-совместимости матки..."
            )
        )

        QTimer.singleShot(
            2200,
            lambda: self.status.setText(
                "Загрузка AI-мантр..."
            )
        )

        QTimer.singleShot(
            3500,
            lambda: self.status.setText(
                "Синхронизация с DeepWomb™ Cluster..."
            )
        )

        QTimer.singleShot(
            5000,
            self.finish_payment
        )

    def finish_payment(self):

        self.paid = True

        self.subscription.setText(
            "🌙 PREMIUM ACTIVE\n"
            "Следующее списание:\n"
            "в следующее полнолуние"
        )

        self.status.setText(
            "✅ Premium-доступ одобрен высшими силами"
        )

    def start_scan(self):

        self.value = 0

        self.progress.setValue(0)

        self.timer.start(60)

    def fake_scan(self):

        self.value += 3

        self.progress.setValue(self.value)

        if self.value < 30:

            self.status.setText(
                "AI анализирует маточное поле..."
            )

        elif self.value < 60:

            self.status.setText(
                "Сканирование денежной чакры..."
            )

        elif self.value < 90:

            self.status.setText(
                "Нейросеть луны строит прогноз..."
            )

        if self.value >= 100:

            self.timer.stop()

            self.status.setText(
                random.choice(RESULTS)
            )