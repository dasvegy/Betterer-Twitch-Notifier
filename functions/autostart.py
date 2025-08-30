from functions.colors import Colors
from functions.variables import version_number
import os
import sys

user_os = sys.platform
username = os.getlogin()

desktop_entry = f"""[Desktop Entry]
Type=Application
Version={version_number}
Name=Betterer Twitch Notifier
Comment=Betterer Twitch Notifier -tray
Exec=
StartupNotify=false
Terminal=false%   
"""

if user_os == 'linux':
    # Variables
    AUTOSTART_DIR = os.path.expanduser(f"/home/{username}/.config/autostart")
    DESKTOP_FILE = os.path.join(AUTOSTART_DIR, "BettererTwitchNotifier.desktop")
    AUTOSTART_FILE = os.path.expanduser(f"/home/{username}/.config/autostart/BettererTwitchNotifier.desktop")


def autostart_setup():
    os.makedirs(AUTOSTART_DIR, exist_ok=True)
    with open(DESKTOP_FILE, "w") as f:
        f.write(desktop_entry)

    print(f"{Colors.green}{Colors.bold}Setup complete!{Colors.reset}\n")


def autostart_ui(back_callback):
    autostart_yesorno = input(f"{Colors.orange}{Colors.bold}Autostart Setup{Colors.reset}"
                              f"\n------------------------\n"
                              f"{Colors.orange}{Colors.bold}"
                              f"Setup Autostart?"
                              f"\n(Yes/No){Colors.reset}"
                              f"\n\n> ")

    if autostart_yesorno == "yes" or autostart_yesorno == "Yes":
        # Clear the Terminal
        os.system('cls' if os.name == 'nt' else 'clear')

        # Linux
        if user_os == 'linux':
            print(f"{Colors.orange}{Colors.bold}Autostart Setup{Colors.reset}"
                  f"\n------------------------")

            # Check if autostart is already setup and give the user the choice what it should to do
            if os.path.exists(AUTOSTART_FILE):
                autostart_exists_prompt = input(f"Autostart already setup\n"
                                                f"\n1. Setup again"
                                                f"\n2. Remove autostart"
                                                f"\n> ")


                if autostart_exists_prompt == "1":
                    autostart_setup()
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(f"{Colors.orange}{Colors.bold}Autostart Setup{Colors.reset}"
                          f"\n------------------------"
                          f"\n{Colors.green}{Colors.bold}Setup complete!{Colors.reset}\n")
                elif autostart_exists_prompt == "2":
                    os.remove(AUTOSTART_FILE)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(f"{Colors.orange}{Colors.bold}Autostart Setup{Colors.reset}"
                          f"\n------------------------"
                          f"\n{Colors.green}{Colors.bold}Setup complete!{Colors.reset}\n")
                else:
                    pass

            else:
                autostart_setup()

        # macOS
        elif user_os == 'darwin':
            print(f"{Colors.blue}{Colors.bold}macOS cumming soon{Colors.reset}")

        # Windows
        elif user_os == 'win32':
            print(f"{Colors.blue}{Colors.bold}Windows cumming soon{Colors.reset}")
        else:
            print(f"{Colors.red}{Colors.bold}Error: OS not recognised{Colors.reset}")
