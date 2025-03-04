from PySide6.QtWidgets import QApplication, QMainWindow
import sys

from main_page import MainPage


class TemporalProcessorUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.main_page = MainPage()
        self.setCentralWidget(self.main_page)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setApplicationName("TemporalProcessorUI")
    window = TemporalProcessorUI()
    window.show()
    sys.exit(app.exec())
