from PyQt5.QtWidgets import QLineEdit, QPushButton, QHBoxLayout
from PyQt5.QtCore import QUrl

class Toolbar(QHBoxLayout):
    def __init__(self, webview):
        super().__init__()
        self.webview = webview

        self.back = QPushButton("←")
        self.forward = QPushButton("→")
        self.reload = QPushButton("⟳")
        self.url_bar = QLineEdit()
        self.go = QPushButton("Git")

        self.addWidget(self.back)
        self.addWidget(self.forward)
        self.addWidget(self.reload)
        self.addWidget(self.url_bar)
        self.addWidget(self.go)

        # Buton işlevleri
        self.back.clicked.connect(self.webview.back)
        self.forward.clicked.connect(self.webview.forward)
        self.reload.clicked.connect(self.webview.reload)
        self.go.clicked.connect(self.navigate_to_url)
        self.url_bar.returnPressed.connect(self.navigate_to_url)

        # Sayfa değişince adres çubuğunu güncelle
        self.webview.urlChanged.connect(self.update_url_bar)

    def navigate_to_url(self):
        url = self.url_bar.text()
        if not url.startswith("http"):
            url = "https://" + url
        self.webview.setUrl(QUrl(url))

    def update_url_bar(self, qurl):
        self.url_bar.setText(qurl.toString())
