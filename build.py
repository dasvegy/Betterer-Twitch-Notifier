import PyInstaller.__main__
import sys
import os

user_os = sys.platform

if user_os.startswith('linux'):
    target_os = "linux"
elif user_os == 'darwin':
    target_os = "macos"
elif user_os == 'win32':
    target_os = "win"
else:
    raise RuntimeError("Unsupported OS!")

# base directory
BASE_DIR = os.path.abspath(".")

# paths
MAIN_SCRIPT = os.path.join(BASE_DIR, "main.py")
FUNCTIONS_FOLDER = os.path.join(BASE_DIR, "functions")
ICON_ICO = os.path.join(BASE_DIR, "icon.ico")
ICON_PNG = os.path.join(BASE_DIR, "icon.png")

# pyinstaller setup
PyInstaller.__main__.run([
    "--noconfirm",
    "--onefile",
    "--windowed",
    f"--icon={ICON_ICO}",
    "--name=betterertwitchnotifier",

    # Ganze functions/ einbinden
    f"--add-data={FUNCTIONS_FOLDER}:functions",
    f"--add-data={ICON_PNG}:.",
    f"--add-data={ICON_ICO}:.",

    f"--hidden-import=plyer.platforms.{target_os}.notification",

    MAIN_SCRIPT
])

print("Completed the Build!")
