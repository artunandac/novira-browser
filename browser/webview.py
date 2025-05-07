from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEnginePage
from PyQt5.QtCore import QUrl
from browser.logger import logger, csp_logger, media_logger

level_map = {
    0: "Info",
    1: "Warning",
    2: "Error"
}

class CustomPage(QWebEnginePage):
    def javaScriptConsoleMessage(self, level, msg, line, source_id):
        level_text = level_map.get(int(level), f"Unknown({int(level)})")
        log_message = f"JS Console [{level_text}] in {source_id}:{line} → {msg}"

        # Filtreleme ve yönlendirme
        if "Content Security Policy" in msg:
            csp_logger.warning(log_message)
        elif "FFmpegDemuxer" in msg or "pipeline_error" in msg:
            media_logger.warning(log_message)
        else:
            logger.warning(log_message)

class WebView(QWebEngineView):
    def __init__(self):
        super().__init__()
        self.setPage(CustomPage(self))
        self.setUrl(QUrl("https://duckduckgo.com"))
