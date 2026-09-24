from functions.colors import Colors
from functions.variables import version_number
from functions.variables import name
import os
import sys

# Get username and Operating System
user_os = sys.platform
username = os.getlogin()

# .desktop file for Linux
desktop_entry = f"""[Desktop Entry]
Comment=Twitch Notifications
Exec=$HOME/.local/bin/betterertwitchnotifier
Icon=/home/konstantin/.config/betterertwitchnotifier/icon.ico
Name=Betterer Twitch Notifier
NoDisplay=false
Path=
PrefersNonDefaultGPU=false
StartupNotify=true
Terminal=false
TerminalOptions=
Type=Application
X-KDE-SubstituteUID=false
X-KDE-Username=

Actions=terminal;tray

[Desktop Action terminal]
Exec=$HOME/.local/bin/betterertwitchnotifier -tui
Icon=utilities-terminal
Name=Start in Terminal
Terminal=true

[Desktop Action tray]
Exec=$HOME/.local/bin/betterertwitchnotifier -tray
Name=Start in Tray (not working atm)
Icon=applications-education-symbolic
"""

def desktop_entry_setup(SHOTCUT_DIR, DESKTOP_FILE):
    os.makedirs(SHOTCUT_DIR, exist_ok=True)
    with open(DESKTOP_FILE, "w") as f:
        f.write(desktop_entry)

    print(f"{Colors.green}{Colors.bold}Setup complete!{Colors.reset}\n")


def autostart_ui(whatitis, back_callback):
    autostart_yesorno = input(f"{Colors.orange}{Colors.bold}{whatitis} Setup{Colors.reset}"
                              f"\n------------------------\n"
                              f"{Colors.orange}{Colors.bold}"
                              f"Setup {whatitis}?"
                              f"\n(Yes/No){Colors.reset}"
                              f"\n\n> ")

    if autostart_yesorno == "yes" or autostart_yesorno == "Yes":
        # Clear the Terminal
        os.system('cls' if os.name == 'nt' else 'clear')

        # Linux
        if user_os == 'linux':
            if whatitis == "Desktop Shortcut":
                SHOTCUT_DIR = os.path.expanduser(f"/home/{username}/.local/share/applications")
                DESKTOP_FILE = os.path.join(SHOTCUT_DIR, "betterertwitchnotifier.desktop")
                DOT_DESKTOP_FULL_DIR = os.path.expanduser(
                    f"/home/{username}/.local/share/applications/betterertwitchnotifier.desktop")
            elif whatitis == "Autostart":
                SHOTCUT_DIR = os.path.expanduser(f"/home/{username}/.config/autostart")
                DESKTOP_FILE = os.path.join(SHOTCUT_DIR, "betterertwitchnotifier.desktop")
                DOT_DESKTOP_FULL_DIR = os.path.expanduser(
                    f"/home/{username}/.config/autostart/betterertwitchnotifier.desktop")

            print(f"{Colors.orange}{Colors.bold}{whatitis} Setup{Colors.reset}"
                  f"\n------------------------")

            # Check if autostart is already setup and give the user the choice what it should to do
            if os.path.exists(DOT_DESKTOP_FULL_DIR):
                autostart_exists_prompt = input(f"{whatitis} already setup\n"
                                                f"\n1. Setup again"
                                                f"\n2. Remove {whatitis}"
                                                f"\nB. Go Back"
                                                f"\n> ")

                if autostart_exists_prompt == "1":
                    desktop_entry_setup(SHOTCUT_DIR, DESKTOP_FILE)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(f"{Colors.orange}{Colors.bold}{whatitis} Setup{Colors.reset}"
                          f"\n------------------------"
                          f"\n{Colors.green}{Colors.bold}Setup complete!{Colors.reset}\n")
                elif autostart_exists_prompt == "2":
                    os.remove(DOT_DESKTOP_FULL_DIR)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(f"{Colors.orange}{Colors.bold}{whatitis} Setup{Colors.reset}"
                          f"\n------------------------"
                          f"\n{Colors.green}{Colors.bold}Setup complete!{Colors.reset}\n")
                elif autostart_exists_prompt == "B":
                    back_callback()
                else:
                    pass

            else:
                desktop_entry_setup(SHOTCUT_DIR, DESKTOP_FILE)

        # macOS
        elif user_os == 'darwin':
            print(f"{Colors.blue}{Colors.bold}macOS cumming soon{Colors.reset}")

        # Windows
        elif user_os == 'win32':
            print(f"{Colors.blue}{Colors.bold}Windows cumming soon{Colors.reset}")
        else:
            print(f"{Colors.red}{Colors.bold}Error: OS not recognised{Colors.reset}")
