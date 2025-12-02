import os, sys
from functions.variables import name_nospace

if sys.platform == "linux":
    config_dir = os.path.join(os.path.expanduser("~"), ".config", name_nospace)
elif sys.platform == "win32":
    config_dir = os.path.join(os.environ.get("APPDATA", os.path.expanduser("~")), name_nospace)
elif sys.platform == "darwin":
    config_dir = os.path.join(os.path.expanduser("~"), "Library", "Application Support", name_nospace)
else:
    raise RuntimeError(f"Unsupported OS: {sys.platform}")

print(config_dir + "/icon.png")
