import PyInstaller.__main__
import os

user_os = sys.platform

if user_os == 'linux':
    os = "linux"
elif user_os == 'darwin':
    os = "macos"
elif user_os == 'win32':
    os = "win"
else:
    print("Unsupported OS!")

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
    "--name=Betterer Twitch Notifier",

    # Ganze functions/ einbinden
    f"--add-data={FUNCTIONS_FOLDER}:functions",
    f"--add-data={ICON_PNG}:.",
    f"--add-data={ICON_ICO}:.",

    f"--hidden-import=plyer.platforms.{os}.notification",

    MAIN_SCRIPT
])

print("Completed the Build!")
