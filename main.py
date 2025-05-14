import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from browser.tabmanager import TabManager  
from browser.layout import BrowserWindow

import sys
import os

# STDERR terminalden logs/errors.log dosyasına yönlendirilir
sys.stderr = open(os.path.join("logs", "errors.log"), "a", encoding="utf-8")

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Novira Browser")

        central = QWidget()
        layout = QVBoxLayout(central)

        self.tabs = TabManager()
        layout.addWidget(self.tabs)

        self.setCentralWidget(central)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
