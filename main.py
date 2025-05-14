import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget,QHBoxLayout, QPushButton
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
        main_layout = QVBoxLayout(central)
        
        # top_layout = QHBoxLayout()

        # self.tabs = TabManager()
        # add_tab_button = QPushButton("➕")
        # add_tab_button.setFixedWidth(30)
        # add_tab_button.clicked.connect(self.tabs.add_new_tab)

        # top_layout.addWidget(self.tabs)
        # top_layout.addWidget(add_tab_button)

        # main_layout.addLayout(top_layout)
        self.tabs = TabManager()
        main_layout.addWidget(self.tabs)

        self.setCentralWidget(central)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
