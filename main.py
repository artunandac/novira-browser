import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QVBoxLayout, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl

from PyQt5 import QtWebEngine
QtWebEngine.QtWebEngine.initialize()




class Novira(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Novira Browser")
        self.setGeometry(100, 100, 1200, 800)

        # Ana widget ve layout
        self.main_widget = QWidget()
        self.layout = QVBoxLayout()

        # Arama çubuğu
        self.search_bar = QLineEdit()
        self.search_bar.setPlaceholderText("Bir şeyler ara veya URL yaz...")
        self.search_bar.returnPressed.connect(self.load_url)

        # Tarayıcı görünümü
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://duckduckgo.com"))

        # Layout'a ekle
        self.layout.addWidget(self.search_bar)
        self.layout.addWidget(self.browser)
        self.main_widget.setLayout(self.layout)

        self.setCentralWidget(self.main_widget)

    def load_url(self):
        text = self.search_bar.text()
        if "." in text or text.startswith("http"):
            url = QUrl(text if text.startswith("http") else "http://" + text)
        else:
            url = QUrl(f"https://www.duckduckgo.com/?q={text}")
        self.browser.setUrl(url)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Novira()
    window.show()
    sys.exit(app.exec_())
