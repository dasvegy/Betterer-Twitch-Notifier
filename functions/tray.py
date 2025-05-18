from functions.tui import tui
from pystray import MenuItem as item
from pystray import Menu as menu
from PIL import Image
import pystray
import asyncio

#
# Ey das kann man jetzt ganz gediegen meine eier lecken
# mir geht diese tray scheiße voll auf den sack
#

def on_clicked(icon, item):
    if item.text == "Betterer Twitch Notifyer":
        print("DEINE MUTTER")
    elif item.text == "Open tui":
        asyncio.run(tui())
    else:
        print(f'Clicked on {item}')

menu_items = [
    item('Betterer Twitch Notifyer', on_clicked),
    menu.SEPARATOR,
    item('Open tui', on_clicked),
    menu.SEPARATOR,
    item('Quit', lambda icon, item: tray.stop()),
]

tray = pystray.Icon("Betterer Twitch Notifyer", Image.open("icon.png"), "Betterer Twitch Notifyer", menu=menu(*menu_items))

def run_tray():
    tray.run()
