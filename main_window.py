from PyQt6.QtWidgets import (
    QMainWindow,
    QStackedWidget
)

from welcome_screen import WelcomeScreen
from payment_screen import PaymentScreen
from ritual_screen import RitualScreen


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Маточный Поток Ultra Premium")
        self.resize(1500, 900)

        self.stack = QStackedWidget()

        self.welcome = WelcomeScreen(self.goto_payment)
        self.payment = PaymentScreen(self.goto_ritual)
        self.ritual = RitualScreen()

        self.stack.addWidget(self.welcome)
        self.stack.addWidget(self.payment)
        self.stack.addWidget(self.ritual)

        self.setCentralWidget(self.stack)

    def goto_payment(self):
        self.stack.setCurrentWidget(self.payment)

    def goto_ritual(self):
        self.stack.setCurrentWidget(self.ritual)