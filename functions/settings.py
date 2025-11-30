from functions.colors import Colors
from functions.autostart import autostart_ui
from functions.variables import version_number
from functions.variables import name_nospace
import json
import os
import sys

user_os = sys.platform

preset = {
    "interval_minutes": 15,
}

json_preset = json.dumps(preset, indent=4)


def get_settings_path(filename="settings.json"):
    if sys.platform == "linux":
        config_dir = os.path.join(os.path.expanduser("~"), ".config", name_nospace)
    elif sys.platform == "win32":
        config_dir = os.path.join(os.environ.get("APPDATA", os.path.expanduser("~")), name_nospace)
    elif sys.platform == "darwin":
        config_dir = os.path.join(os.path.expanduser("~"), "Library", "Application Support", name_nospace)
    else:
        raise RuntimeError(f"Unsupported OS: {sys.platform}")

    os.makedirs(config_dir, exist_ok=True)
    file_path = os.path.join(config_dir, filename)

    if not os.path.exists(file_path):
        with open(file_path, "w") as f:
            f.write(json_preset)
        print(f"{file_path} created")

    return file_path


settings_file_path = get_settings_path("settings.json")

with open(settings_file_path, "r") as file:
    settings_file = json.load(file)
    interval_minutes = float(settings_file["interval_minutes"])


# Writing the Setting into the settings.json file
def write_setting(setting_to_change, arg_to_change):
    with open(settings_file_path, "r") as file:
        settings_file = json.load(file)
        print(f"\nSetting before: {Colors.orange}{Colors.bold}{settings_file[setting_to_change]}{Colors.reset}")

        settings_file[setting_to_change] = arg_to_change

        with open(settings_file_path, "w") as file:
            json.dump(settings_file, file, indent=4)

        print(f"Setting after: {Colors.orange}{Colors.bold}{settings_file[setting_to_change]}{Colors.reset}")


def settings(back_callback):
    # Clear the Terminal
    os.system('cls' if os.name == 'nt' else 'clear')

    # Settings page
    option = input(f"{Colors.purple}{Colors.bold}Betterer Twitch Notifier{Colors.reset}"
                   "\n------------------------ "
                   "\n1. Change how long should it wait till it checks for online Streamers"
                   "\n2. Autostart on Login"
                   "\n3. Information"
                   "\n\nB: Go Back "
                   "\nQ: Quit "
                   "\n> ")

    # Frequancy Setting
    if option == "1":
        os.system('cls' if os.name == 'nt' else 'clear')
        frequency_setting = int(input(
            f"{Colors.orange}{Colors.bold}Enter the number of minutes to wait before checking for online streamers"
            f"\n(In minutes){Colors.reset}"
            f"\n\n> "))
        write_setting("interval_minutes", frequency_setting)
        input(f"{Colors.orange}Press {Colors.bold}Enter {Colors.reset}{Colors.orange}to go back...{Colors.reset}")
        back_callback()

    # Autostart Setting
    elif option == "2":
        os.system('cls' if os.name == 'nt' else 'clear')
        autostart_ui(settings)

        input(f"{Colors.orange}Press {Colors.bold}Enter {Colors.reset}{Colors.orange}to go back...{Colors.reset}")
        back_callback()

    # Information Page
    elif option == "3":
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"{Colors.purple}{Colors.bold}Betterer Twitch Notifier{Colors.reset}"
              "\n------------------------ "
              f"\nVersion:          {Colors.orange}{version_number}{Colors.reset}"
              f"\nBy:               {Colors.orange}vegy (aka dasvegy){Colors.reset}"
              f"\nOfficial Page:    {Colors.orange}https://github.com/dasvegy/Betterer-Twitch-Notifier{Colors.reset}"
              f"\n\n ")

        input(f"{Colors.orange}Press {Colors.bold}Enter {Colors.reset}{Colors.orange}to go back...{Colors.reset}")
        back_callback()

    # Going Back
    elif option == "b" or option == "B":
        back_callback()

    # Quitting
    elif option == "q" or option == "Q":
        print(f"{Colors.red}{Colors.bold}Exiting...{Colors.reset}")
        sys.exit(0)

    # Error so it won't crash
    else:
        print(f"\n{Colors.red}{Colors.bold}Error: Nothing Selected or user was to dumb to type right{Colors.reset}")
