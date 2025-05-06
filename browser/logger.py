import logging
import os
from datetime import datetime

# Log klasörü yoksa oluştur
log_dir = os.path.join(os.path.dirname(__file__), "..", "logs")
os.makedirs(log_dir, exist_ok=True)

# Log dosyası ismi
log_file = os.path.join(log_dir, "app.log")

# Logger oluştur
logger = logging.getLogger("luvira")
logger.setLevel(logging.DEBUG)  # DEBUG seviyesinde her şeyi yakala

# Dosyaya yazan handler
file_handler = logging.FileHandler(log_file, encoding="utf-8")
file_handler.setLevel(logging.DEBUG)

# Format belirle
formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')
file_handler.setFormatter(formatter)

# Terminale de yaz
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.ERROR)  # Sadece ERROR ve üstü terminale

# Logger'a ekle
logger.addHandler(file_handler)
logger.addHandler(console_handler)
