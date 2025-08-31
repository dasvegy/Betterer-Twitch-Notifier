from functions.variables import name
from pystray import MenuItem as item
from pystray import Menu as menu
from PIL import Image
import pystray
import asyncio


def on_clicked(icon, item):
    if item.text == "Betterer Twitch Notifier":
        pass
    else:
        print(f'Clicked on {item}')


menu_items = [
    item(name, on_clicked),
    menu.SEPARATOR,
    item('Quit', lambda icon, item: tray.stop()),
]

tray = pystray.Icon(name, Image.open("icon.png"), name,
                    menu=menu(*menu_items))


def run_tray():
    tray.run()
