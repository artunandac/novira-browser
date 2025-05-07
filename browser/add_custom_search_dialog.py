from PyQt5.QtWidgets import (
    QDialog, QVBoxLayout, QLabel, QLineEdit, QDialogButtonBox
)

class AddCustomSearchDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Özel Arama Motoru Ekle")
        self.setFixedSize(400, 180)

        layout = QVBoxLayout()

        # Arama motoru adı
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Örnek: MySearch")

        # URL şablonu
        self.url_input = QLineEdit()
        self.url_input.setPlaceholderText("Örnek: https://example.com/search?q=")

        layout.addWidget(QLabel("Arama motorunun adı:"))
        layout.addWidget(self.name_input)

        layout.addWidget(QLabel("Arama URL şablonu:"))
        layout.addWidget(self.url_input)

        # Butonlar
        self.buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.buttons.accepted.connect(self.accept)
        self.buttons.rejected.connect(self.reject)

        layout.addWidget(self.buttons)
        self.setLayout(layout)

    def get_data(self):
        return self.name_input.text(), self.url_input.text()
