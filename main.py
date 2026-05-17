import sys
from PyQt6.QtWidgets import QApplication
from main_window import MainWindow


def load_stylesheet() -> str:
    with open("main.qss", "r", encoding="utf-8") as f:
        return f.read()


def main():
    app = QApplication(sys.argv)

    app.setStyleSheet(load_stylesheet())

    window = MainWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()