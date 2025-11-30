from functions.variables import name
import PyInstaller.__main__
import sys
import os

user_os = sys.platform

# base directory
BASE_DIR = os.path.abspath(".")

# paths
MAIN_SCRIPT = os.path.join(BASE_DIR, "main.py")
FUNCTIONS_FOLDER = os.path.join(BASE_DIR, "functions")
ICON_ICO = os.path.join(BASE_DIR, "icon.ico:.")
ICON_PNG = os.path.join(BASE_DIR, "icon.png:.")

if user_os.startswith('linux'):
    target_os = "linux"
elif user_os == 'darwin':
    target_os = "macos"
elif user_os == 'win32':
    target_os = "win"
    ICON_ICO = os.path.join(BASE_DIR, "icon.ico")
    ICON_PNG = os.path.join(BASE_DIR, "icon.png")
else:
    raise RuntimeError("Unsupported OS!")

print("IconPNG: " + ICON_PNG)

if user_os == 'win32':
    # pyinstaller setup
    PyInstaller.__main__.run([
        "--strip",
        "--noconfirm",
        "--onefile",
        "--windowed",
        f"--icon={ICON_ICO}",
        f"--name={name}",

        f"--add-data={FUNCTIONS_FOLDER}:functions",
        f"--add-data={ICON_PNG};.",
        f"--add-data={ICON_ICO};.",

        f"--hidden-import=plyer.platforms.{target_os}.notification",

        MAIN_SCRIPT
    ])
else:
    # pyinstaller setup
    PyInstaller.__main__.run([
        "--strip",
        "--noconfirm",
        "--onefile",
        # "--windowed",
        f"--icon={ICON_ICO}",
        "--name=Betterer Twitch Notifier",

        f"--add-data={FUNCTIONS_FOLDER}:functions",
        f"--add-data={ICON_PNG}",
        f"--add-data={ICON_ICO}",

        f"--hidden-import=plyer.platforms.{target_os}.notification",

        MAIN_SCRIPT
    ])

print("Completed the Build!")
