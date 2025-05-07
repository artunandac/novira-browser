import logging
import os
from datetime import datetime

def create_logger(name, log_filename, level=logging.DEBUG):
    log_dir = os.path.join(os.path.dirname(__file__), "..", "logs")
    os.makedirs(log_dir, exist_ok=True)
    log_file = os.path.join(log_dir, log_filename)

    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Dosyaya yazma
    fh = logging.FileHandler(log_file, encoding="utf-8")
    fh.setLevel(level)
    formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')
    fh.setFormatter(formatter)
    logger.addHandler(fh)

    return logger

# Ana log (her şey burada da olabilir)
logger = create_logger("main", "app.log")

# Alt loglar
csp_logger = create_logger("csp", "csp.log")
media_logger = create_logger("media", "media.log")
