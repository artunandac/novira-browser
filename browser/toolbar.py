# from PyQt5.QtWidgets import (
#     QHBoxLayout, QLineEdit, QPushButton, QComboBox
# )
# from PyQt5.QtCore import QUrl

# from config.search_engine import BUILTIN_ENGINES, load_settings, save_settings, get_search_url
# from browser.add_custom_search_dialog import AddCustomSearchDialog

# class Toolbar(QHBoxLayout):
#     def __init__(self, webview):
#         super().__init__()
#         self.webview = webview

#         # Ayarları yükle
#         self.settings = load_settings()
#         self.custom_engine_url = self.settings.get("custom_search_url", "")
#         last_engine = self.settings.get("default_search_engine", "DuckDuckGo")

#         # Bileşenler
#         self.search_selector = QComboBox()
#         self.search_selector.addItems(BUILTIN_ENGINES.keys())
#         self.search_selector.setCurrentText(last_engine)

#         self.back = QPushButton("←")
#         self.forward = QPushButton("→")
#         self.reload = QPushButton("⟳")
#         self.url_bar = QLineEdit()
#         self.go = QPushButton("Git")

#         # Yerleşim
#         self.addWidget(self.search_selector)
#         self.addWidget(self.back)
#         self.addWidget(self.forward)
#         self.addWidget(self.reload)
#         self.addWidget(self.url_bar)
#         self.addWidget(self.go)

#         # Olaylar
#         self.back.clicked.connect(self.webview.back)
#         self.forward.clicked.connect(self.webview.forward)
#         self.reload.clicked.connect(self.webview.reload)
#         self.go.clicked.connect(self.navigate_to_url)
#         self.url_bar.returnPressed.connect(self.navigate_to_url)
#         self.webview.urlChanged.connect(self.update_url_bar)
#         self.search_selector.currentIndexChanged.connect(self.check_custom_engine)

#     def check_custom_engine(self, index):
#         engine = self.search_selector.currentText()

#         if engine == "Özel...":
#             dialog = AddCustomSearchDialog()
#             if dialog.exec_():
#                 name, url = dialog.get_data()
#                 if name and url:
#                     self.search_selector.insertItem(self.search_selector.count() - 1, name)
#                     self.search_selector.setCurrentText(name)
#                     self.custom_engine_url = url
#                     self.settings["default_search_engine"] = name
#                     self.settings["custom_search_url"] = url
#                     save_settings(self.settings)
#                 else:
#                     self.search_selector.setCurrentIndex(0)
#             else:
#                 self.search_selector.setCurrentIndex(0)
#         else:
#             self.settings["default_search_engine"] = engine
#             save_settings(self.settings)

#     def navigate_to_url(self):
#         query = self.url_bar.text()
#         engine = self.search_selector.currentText()
#         search_url = get_search_url(engine, self.custom_engine_url)
#         if search_url:
#             self.webview.setUrl(QUrl(search_url + query))

#     def update_url_bar(self, qurl):
#         self.url_bar.setText(qurl.toString())

from PyQt5.QtWidgets import (
    QHBoxLayout, QLineEdit, QPushButton, QComboBox, QMenu
)
from PyQt5.QtCore import QUrl
from config.search_engine import BUILTIN_ENGINES, load_settings, save_settings, get_search_url
from browser.add_custom_search_dialog import AddCustomSearchDialog

class Toolbar(QHBoxLayout):
    def __init__(self, webview):
        super().__init__()
        self.webview = webview

        # Ayarları yükle
        self.settings = load_settings()
        self.custom_engines = self.settings.get("custom_engines", {})
        self.custom_engine_url = self.settings.get("custom_search_url", "")
        last_engine = self.settings.get("default_search_engine", "DuckDuckGo")

        # Arama motoru seçici
        self.search_selector = QComboBox()
        self.load_engine_list()
        self.search_selector.setCurrentText(last_engine)

        # Ayarlar butonu (⚙️)
        self.settings_button = QPushButton("⚙️")
        self.settings_button.setFixedWidth(30)
        self.settings_button.clicked.connect(self.show_engine_menu)

        # Diğer bileşenler
        self.back = QPushButton("←")
        self.forward = QPushButton("→")
        self.reload = QPushButton("⟳")
        self.url_bar = QLineEdit()
        self.go = QPushButton("Git")

        # Yerleşim
        self.addWidget(self.search_selector)
        self.addWidget(self.settings_button)
        self.addWidget(self.back)
        self.addWidget(self.forward)
        self.addWidget(self.reload)
        self.addWidget(self.url_bar)
        self.addWidget(self.go)

        # Olaylar
        self.back.clicked.connect(self.webview.back)
        self.forward.clicked.connect(self.webview.forward)
        self.reload.clicked.connect(self.webview.reload)
        self.go.clicked.connect(self.navigate_to_url)
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        self.webview.urlChanged.connect(self.update_url_bar)
        self.search_selector.currentIndexChanged.connect(self.check_custom_engine)

        self.update_settings_button_visibility()

    def load_engine_list(self):
        self.search_selector.clear()

        for name in BUILTIN_ENGINES.keys():
            self.search_selector.addItem(name)

        for name in self.custom_engines.keys():
            self.search_selector.addItem(name)

        self.search_selector.addItem("Özel...")

    def check_custom_engine(self, index):
        engine = self.search_selector.currentText()

        if engine == "Özel...":
            dialog = AddCustomSearchDialog()
            if dialog.exec_():
                name, url = dialog.get_data()
                if name and url:
                    self.custom_engines[name] = url
                    self.custom_engine_url = url
                    self.settings["default_search_engine"] = name
                    self.settings["custom_engines"] = self.custom_engines
                    self.settings["custom_search_url"] = url
                    save_settings(self.settings)
                    self.load_engine_list()
                    self.search_selector.setCurrentText(name)
            else:
                self.search_selector.setCurrentIndex(0)
        else:
            self.settings["default_search_engine"] = engine
            self.settings["custom_search_url"] = self.custom_engines.get(engine, "")
            save_settings(self.settings)

        self.update_settings_button_visibility()

    def navigate_to_url(self):
        query = self.url_bar.text()
        engine = self.search_selector.currentText()
        url = get_search_url(engine, self.custom_engine_url, self.custom_engines)
        if url:
            self.webview.setUrl(QUrl(url + query))

    def update_url_bar(self, qurl):
        self.url_bar.setText(qurl.toString())

    def update_settings_button_visibility(self):
        engine = self.search_selector.currentText()
        self.settings_button.setVisible(engine in self.custom_engines)

    def show_engine_menu(self):
        engine = self.search_selector.currentText()
        if engine not in self.custom_engines:
            return

        menu = QMenu()
        edit_action = menu.addAction("Düzenle")
        delete_action = menu.addAction("Sil")

        action = menu.exec_(self.settings_button.mapToGlobal(self.settings_button.rect().bottomLeft()))

        if action == edit_action:
            dialog = AddCustomSearchDialog()
            dialog.name_input.setText(engine)
            dialog.url_input.setText(self.custom_engines[engine])
            if dialog.exec_():
                new_name, new_url = dialog.get_data()
                if new_name and new_url:
                    del self.custom_engines[engine]
                    self.custom_engines[new_name] = new_url
                    self.settings["default_search_engine"] = new_name
                    self.settings["custom_search_url"] = new_url
                    self.settings["custom_engines"] = self.custom_engines
                    save_settings(self.settings)
                    self.load_engine_list()
                    self.search_selector.setCurrentText(new_name)

        elif action == delete_action:
            del self.custom_engines[engine]
            self.settings["custom_engines"] = self.custom_engines
            self.settings["default_search_engine"] = "DuckDuckGo"
            self.settings["custom_search_url"] = ""
            save_settings(self.settings)
            self.load_engine_list()
            self.search_selector.setCurrentText("DuckDuckGo")

        self.update_settings_button_visibility()
