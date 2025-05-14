from PyQt5.QtWidgets import QTabWidget
from PyQt5.QtCore import pyqtSlot, QUrl
from browser.webview import WebView  # senin mevcut custom WebView sınıfın

from config.search_engine import load_settings  # ayarları oku


class TabManager(QTabWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setTabsClosable(True)
        self.tabCloseRequested.connect(self.close_tab)
        self.currentChanged.connect(self.on_tab_changed)

        # İlk sekmeyi aç
        settings = load_settings()
        startup_url = settings.get("startup_url", "https://duckduckgo.com")
        self.add_new_tab(startup_url)

    def add_new_tab(self, url=None, title="Yeni Sekme"):
        settings = load_settings()
        url = settings.get("startup_url", "https://duckduckgo.com")

        webview = WebView()
        webview.setUrl(QUrl(url))
        index = self.addTab(webview, title)
        self.setCurrentIndex(index)

    @pyqtSlot(int)
    def on_tab_changed(self, index):
        for i in range(self.count()):
            webview = self.widget(i)
            if i == index:
                webview.setVisible(True)
                # Yeniden başlat (isteğe bağlı)
                # webview.reload()
            else:
                webview.setVisible(False)
                webview.page().runJavaScript("window.stop();")

    def close_tab(self, index):
        widget = self.widget(index)
        if widget:
            widget.deleteLater()
        self.removeTab(index)
