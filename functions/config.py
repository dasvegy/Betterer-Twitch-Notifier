import os
import sys
import json
from functions.variables import name_nospace


def get_config_path():
    if sys.platform.startswith("linux"):
        config_dir = os.path.join(os.path.expanduser("~"), ".config", name_nospace)
    elif sys.platform == "win32":
        config_dir = os.path.join(os.environ.get("APPDATA", os.path.expanduser("~")), name_nospace)
    elif sys.platform == "darwin":
        config_dir = os.path.join(os.path.expanduser("~"), "Library", "Application Support", name_nospace)
    else:
        raise RuntimeError(f"Unsupported OS: {sys.platform}")

    os.makedirs(config_dir, exist_ok=True)
    return os.path.join(config_dir, "config.json")


def load_config():
    config_path = get_config_path()
    default_config = {
        "interval_minutes": 5
    }

    if not os.path.exists(config_path):
        with open(config_path, "w") as f:
            json.dump(default_config, f, indent=4)
        return default_config

    with open(config_path, "r") as f:
        return json.load(f)
