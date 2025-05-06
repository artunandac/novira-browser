import sys
from PyQt5.QtWidgets import QApplication
from browser.layout import BrowserWindow

import sys
import os

# STDERR terminalden logs/errors.log dosyasına yönlendirilir
sys.stderr = open(os.path.join("logs", "errors.log"), "a", encoding="utf-8")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BrowserWindow()
    window.show()
    sys.exit(app.exec_())
