from PyQt5.QtWidgets import QTabWidget, QApplication, QPushButton, QMenu, QAction, QWidget, QHBoxLayout, QWidgetAction, QLabel
from PyQt5.QtCore import pyqtSlot, QUrl, Qt
from browser.webview import WebView  # senin mevcut custom WebView sınıfın

from config.search_engine import load_settings  # ayarları oku


class TabManager(QTabWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setTabsClosable(True)
        self.tabCloseRequested.connect(self.close_tab)
        self.currentChanged.connect(self.on_tab_changed)
        # self.new_tab_button = QPushButton("➕")
        # self.new_tab_button.setFixedSize(24, 24)
        # self.new_tab_button.clicked.connect(self.add_new_tab)
        # self.setCornerWidget(self.new_tab_button)
        # style = """
        #     QPushButton {
        #         border: none;
        #         font-weight: bold;
        #         font-size: 14px;
        #     }
        #     QPushButton:hover {
        #         background-color: #e0e0e0;
        #     }
        # """
        self.new_tab_button = QPushButton("➕")
        self.new_tab_button.setFixedSize(28, 28)
        # self.new_tab_button.setStyleSheet(style)
        self.new_tab_button.clicked.connect(self.add_new_tab)

        # ⋮ Menü butonu
        self.menu_button = QPushButton("⋮")
        self.menu_button.setFixedSize(28, 28)
        # self.menu_button.setStyleSheet(style)
        self.menu_button.setMenu(self.build_menu())  # Menüyi bağla

        # Hepsini yerleştirecek kutu
        corner_container = QWidget()
        corner_layout = QHBoxLayout(corner_container)
        corner_layout.setContentsMargins(0, 0, 0, 0)
        corner_layout.setSpacing(2)
        corner_layout.addWidget(self.new_tab_button)
        corner_layout.addWidget(self.menu_button)

        # Sekme çubuğunun sağına yerleştir
        self.setCornerWidget(corner_container)

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

        if self.count() == 0 and self.parent():
            QApplication.quit()

    def build_menu(self):
        menu = QMenu()

        action_new_tab = QAction("🆕 Yeni Sekme", self)
        action_new_tab.triggered.connect(self.add_new_tab)

        action_settings = QAction("⚙️ Ayarlar", self)
        action_settings.triggered.connect(self.add_new_tab)

        action_fullscreen = QAction("⛶ Tam Ekran", self)
        action_fullscreen.triggered.connect(self.add_new_tab)

        action_zoom_in = QAction("➕ Yaklaştır", self)
        action_zoom_in.triggered.connect(lambda: self.zoom(0.1))

        action_zoom_out = QAction("➖ Uzaklaştır", self)
        action_zoom_out.triggered.connect(lambda: self.zoom(-0.1))

        # Menüye ekle
        menu.addAction(action_new_tab)
        menu.addSeparator()
        menu.addAction(action_settings)
        menu.addSeparator()
        menu.addAction(action_fullscreen)
        menu.addAction(action_zoom_in)
        menu.addAction(action_zoom_out)
        menu.addAction(self.create_zoom_widget())


        return menu
    
    def create_zoom_widget(self):
        zoom_widget = QWidget()
        layout = QHBoxLayout(zoom_widget)
        layout.setContentsMargins(5, 5, 5, 5)
        layout.setSpacing(4)

        self.zoom_label = QLabel("100%")
        self.zoom_label.setFixedWidth(50)
        self.zoom_label.setAlignment(Qt.AlignCenter)

        btn_minus = QPushButton("➖")
        btn_plus = QPushButton("➕")

        btn_minus.clicked.connect(lambda: self.zoom(-0.1))
        btn_plus.clicked.connect(lambda: self.zoom(0.1))

        layout.addWidget(btn_minus)
        layout.addWidget(self.zoom_label)
        layout.addWidget(btn_plus)

        zoom_action = QWidgetAction(self)
        zoom_action.setDefaultWidget(zoom_widget)
        return zoom_action
    
    # def zoom(self, delta):
        current_index = self.currentIndex()
        if current_index >= 0:
            webview = self.widget(current_index)
            current_zoom = webview.zoomFactor()
            webview.setZoomFactor(current_zoom + delta)

    def zoom(self, delta):
        current_index = self.currentIndex()
        if current_index >= 0:
            webview = self.widget(current_index)
            current_zoom = webview.zoomFactor()
            new_zoom = max(0.25, min(5.0, current_zoom + delta))  # sınır: %25 - %500
            webview.setZoomFactor(new_zoom)

            # Yüzde olarak yazdır
            if hasattr(self, 'zoom_label'):
                self.zoom_label.setText(f"{int(new_zoom * 100)}%")
