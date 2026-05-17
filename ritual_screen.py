from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QMessageBox,
    QHBoxLayout,
    QProgressBar,
    QScrollArea,
    QSizePolicy
)

from PyQt6.QtCore import QTimer
from PyQt6.QtCore import QTimer, Qt

from glow_button import GlowButton
from energy_chart import EnergyChart
from moon_widget import MoonWidget
from fake_scanner import FakeScanner
from premium_scanner import PremiumScanner

from phrases import random_phrase


class RitualScreen(QWidget):

    def __init__(self):
        super().__init__()

        # Главный layout окна
        root_layout = QVBoxLayout(self)

        # Scroll area
        scroll = QScrollArea()

        scroll.setWidgetResizable(True)

        scroll.setHorizontalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAlwaysOff
        )
        scroll.setVerticalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAsNeeded
            )
        root_layout.addWidget(scroll)

        # Контент внутри scroll
        container = QWidget()

        scroll.setWidget(container)

        self.main_layout = QVBoxLayout(container)

        self.main_layout.setSpacing(20)

        self.title = QLabel(
            "КВАНТОВОЕ РАСКРЫТИЕ МАТКИ"
        )

        self.title.setObjectName("title")

        self.main_layout.addWidget(self.title)

        self.timer_label = QLabel(
            "До открытия потока: 11:11:11"
        )

        self.main_layout.addWidget(
            self.timer_label
        )

        self.connection = QLabel(
            "Связь с космосом: СТАБИЛЬНА"
        )

        self.main_layout.addWidget(
            self.connection
        )

        self.text = QLabel("""
Матка может быть открыта только:
- на убывающую луну
- в конце января
- в солнечную погоду
- при грибном дожде
- после достижения 25-летнего возраста
- на 4 день месячных

Только в этом случае открывается денежный поток и поток сознания.
""")

        self.text.setWordWrap(True)

        self.main_layout.addWidget(
            self.text
        )

        self.energy = QProgressBar()
        self.energy.setValue(78)

        self.main_layout.addWidget(
            self.energy
        )

        self.chart = EnergyChart()

        self.chart.setMinimumHeight(300)

        self.main_layout.addWidget(
            self.chart
        )

        self.moon = MoonWidget()

        self.moon.setMinimumHeight(220)

        self.main_layout.addWidget(
            self.moon
        )

        self.scanner = FakeScanner()

        self.scanner.setMinimumHeight(140)

        self.main_layout.addWidget(
            self.scanner
        )

        self.premium = PremiumScanner()

        self.main_layout.addWidget(
            self.premium
        )

        buttons_layout = QHBoxLayout()

        ritual_buttons = [
            "Открыть квантовую матку",
            "Синхронизировать денежные вибрации",
            "Очистить чакру налоговой",
            "Активировать поток изобилия"
        ]

        for txt in ritual_buttons:

            btn = GlowButton(txt)

            btn.clicked.connect(
                self.perform_ritual
            )

            buttons_layout.addWidget(btn)

        self.main_layout.addLayout(
            buttons_layout
        )

        self.main_layout.addStretch()

        self.start_fake_timer()

    def perform_ritual(self):

        msg = QMessageBox(self)

        msg.setWindowTitle(
            "Космическая активация"
        )

        msg.setText(
            random_phrase()
        )

        msg.exec()

    def start_fake_timer(self):

        self.seconds = 40000

        self.timer = QTimer()

        self.timer.timeout.connect(
            self.update_timer
        )

        self.timer.start(1000)

    def update_timer(self):

        self.seconds -= 1

        h = self.seconds // 3600
        m = (self.seconds % 3600) // 60
        s = self.seconds % 60

        self.timer_label.setText(
            f"До открытия потока: "
            f"{h:02}:{m:02}:{s:02}"
        )