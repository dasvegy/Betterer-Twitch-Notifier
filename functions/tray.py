import os
import sys
import pystray
import threading
from PIL import Image
from pystray import Menu, MenuItem
from functions.variables import name, name_nospace
import functions.loop as loop


def quit_everything(icon, item):
    print("sigma")
    loop.stop_loop = True
    tray.stop()


def on_clicked(icon, item):
    if item.text == "Betterer Twitch Notifier":

    else:
        print(f'Clicked on {item}')


menu_items = [
    MenuItem(name, on_clicked),
    Menu.SEPARATOR,
    MenuItem('Quit', quit_everything),
]


if sys.platform == "linux":
    config_dir = os.path.join(os.path.expanduser("~"), ".config", name_nospace)
elif sys.platform == "win32":
    config_dir = os.path.join(os.environ.get("APPDATA", os.path.expanduser("~")), name_nospace)
elif sys.platform == "darwin":
    config_dir = os.path.join(os.path.expanduser("~"), "Library", "Application Support", name_nospace)
else:
    raise RuntimeError(f"Unsupported OS: {sys.platform}")

icon = config_dir + "/icon.png"
tray = pystray.Icon(name, Image.open(icon), name, menu=Menu(*menu_items))


def run_tray():
    threading.Thread(target=tray.run, daemon=True).start()
