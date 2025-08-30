from functions.colors import Colors
from functions.autostart import autostart_ui
from functions.variables import version_number
import json
import os


# Writing the Setting into the settings.json file
def write_setting(setting_to_change, arg_to_change):
    with open("settings.json", "r") as file:
        settings_file = json.load(file)
        print(f"\nSetting before: {Colors.orange}{Colors.bold}{settings_file[setting_to_change]}{Colors.reset}")

        settings_file[setting_to_change] = arg_to_change

        with open("settings.json", "w") as file:
            json.dump(settings_file, file, indent=4)

        print(f"Setting after: {Colors.orange}{Colors.bold}{settings_file[setting_to_change]}{Colors.reset}")


def settings(back_callback):
    # Clear the Terminal
    os.system('cls' if os.name == 'nt' else 'clear')

    # Settings page
    option = input(f"{Colors.purple}{Colors.bold}Betterer Twitch Notifyer{Colors.reset}"
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
        frequency_setting = input(
            f"{Colors.orange}{Colors.bold}How long should it wait till it checks for online Streamers?"
            f"\n(In minutes){Colors.reset}"
            f"\n\n> ")
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
        print(f"{Colors.purple}{Colors.bold}Betterer Twitch Notifyer{Colors.reset}"
              "\n------------------------ "
              f"\nVersion:          {Colors.orange}{version_number}{Colors.reset}"
              f"\nBy:               {Colors.orange}vegy (aka dasvegy){Colors.reset}"
              f"\nOfficial Page:    {Colors.orange}https://github.com/dasvegy/Betterer-Twitch-Notifyer{Colors.reset}"
              f"\n\n ")

        input(f"{Colors.orange}Press {Colors.bold}Enter {Colors.reset}{Colors.orange}to go back...{Colors.reset}")
        back_callback()

    # Going Back
    elif option == "b" or option == "B":
        back_callback()

    # Quitting
    elif option == "q" or option == "Q":
        print(f"{Colors.red}{Colors.bold}Exiting...{Colors.reset}")
        quit()

    # Error so it won't crash
    else:
        print(f"\n{Colors.red}{Colors.bold}Error: Nothing Selected or user was to dumb to type right{Colors.reset}")
