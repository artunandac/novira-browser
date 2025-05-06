from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEnginePage
from PyQt5.QtCore import QUrl
from browser.logger import logger

level_map = {
    0: "Info",
    1: "Warning",
    2: "Error"
}

class CustomPage(QWebEnginePage):
    def javaScriptConsoleMessage(self, level, msg, line, source_id):
        level_text = level_map.get(int(level), f"Unknown({int(level)})")
        logger.warning(f"JS Console [{level_text}] in {source_id}:{line} → {msg}")

class WebView(QWebEngineView):
    def __init__(self):
        super().__init__()
        self.setPage(CustomPage(self))
        self.setUrl(QUrl("https://duckduckgo.com"))
