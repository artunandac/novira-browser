import sys
from PyQt5.QtWidgets import QApplication
from browser.layout import BrowserWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BrowserWindow()
    window.show()
    sys.exit(app.exec_())
