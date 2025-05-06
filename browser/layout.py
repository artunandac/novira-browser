from PyQt5.QtWidgets import QWidget, QVBoxLayout
from browser.webview import WebView
from browser.toolbar import Toolbar

class BrowserWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Luvira Tarayıcı")
        self.resize(1000, 700)

        self.webview = WebView()
        self.toolbar = Toolbar(self.webview)

        layout = QVBoxLayout()
        layout.addLayout(self.toolbar)
        layout.addWidget(self.webview)

        self.setLayout(layout)
