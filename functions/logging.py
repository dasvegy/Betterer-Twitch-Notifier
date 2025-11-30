import os
import sys

import logging
from functions.variables import name_nospace


def get_logging_path(filename="better.log"):
    if sys.platform == "linux":
        config_dir = os.path.join(os.path.expanduser("~"), ".config", name_nospace)
    elif sys.platform == "win32":
        config_dir = os.path.join(os.environ.get("APPDATA", os.path.expanduser("~")), name_nospace)
    elif sys.platform == "darwin":
        config_dir = os.path.join(os.path.expanduser("~"), "Library", "Application Support", name_nospace)
    else:
        raise RuntimeError(f"Unsupported OS: {sys.platform}")

    os.makedirs(config_dir, exist_ok=True)
    file_path = os.path.join(config_dir, filename)

    if not os.path.exists(file_path):
        with open(file_path, "w", encoding="utf-8") as f:
            f.write("")
        print(f"{file_path} created")

    return file_path


LOG_FILE = get_logging_path()

# logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE, encoding="utf-8"),
        # logging.StreamHandler()
    ]
)

logger = logging.getLogger(name_nospace)
