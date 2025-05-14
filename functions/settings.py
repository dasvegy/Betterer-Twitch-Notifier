from functions.colors import Colors
import json
import os

def write_setting(setting_to_change, arg_to_change):
    with open("settings.json", "r") as file:
        settings_file = json.load(file)
        print(f"\nSetting before: {Colors.orange}{Colors.bold}{settings_file[setting_to_change]}{Colors.reset}")

        settings_file[setting_to_change] = arg_to_change

        with open("settings.json", "w") as file:
            json.dump(settings_file, file, indent=4)

        print(f"Setting after: {Colors.orange}{Colors.bold}{settings_file[setting_to_change]}{Colors.reset}")

def settings(back_callback):
    os.system('cls' if os.name == 'nt' else 'clear')
    option = input(f"{Colors.purple}{Colors.bold}Betterer Twitch Notifyer{Colors.reset}"
                    "\n------------------------ "
                    f"\n{Colors.yellow}1. placeholder{Colors.reset}"
                    "\n2. Change how long should it wait till it checks for online Streamers"
                    "\n3. Autostart on Login"
                    "\n4. Information"
                    "\n\nB: Go Back "
                    "\nQ: Quit "
                    "\n> ")

    if option == "1":
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"{Colors.orange}{Colors.bold}leck eier?{Colors.reset}")
    elif option == "2":
        os.system('cls' if os.name == 'nt' else 'clear')
        frequency_setting = input(f"{Colors.orange}{Colors.bold}How long should it wait till it checks for online Streamers?"
                                  f"\n(In minutes){Colors.reset}"
                                  f"\n\n> ")
        write_setting("interval_minutes",frequency_setting)
        input(f"{Colors.orange}Press {Colors.bold}Enter {Colors.reset}{Colors.orange}to go back...{Colors.reset}")
        back_callback()

    elif option == "3":
        os.system('cls' if os.name == 'nt' else 'clear')
        autostart_setting = input(f"{Colors.orange}{Colors.bold}Enable Autostart?"
                                  f"\n(On/Off){Colors.reset}"
                                  f"\n\n> ")
        write_setting("autostart",autostart_setting)

        input(f"{Colors.orange}Press {Colors.bold}Enter {Colors.reset}{Colors.orange}to go back...{Colors.reset}")
        back_callback()

    elif option == "4":
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"{Colors.purple}{Colors.bold}Betterer Twitch Notifyer{Colors.reset}"
              "\n------------------------ "
              f"\nVersion:          {Colors.orange}1.0{Colors.reset}"
              f"\nBy:               {Colors.orange}vegy (aka dasvegy){Colors.reset}"
              f"\nOfficial Page:    {Colors.orange}https://github.com/dasvegy/Betterer-Twitch-Notifyer{Colors.reset}"
              f"\n\n ")

        input(f"{Colors.orange}Press {Colors.bold}Enter {Colors.reset}{Colors.orange}to go back...{Colors.reset}")
        back_callback()


    elif option == "b" or option == "B":
        back_callback()
    elif option == "q" or option == "Q":
        print(f"{Colors.red}{Colors.bold}Exiting...{Colors.reset}")
        quit()
    else:
        print(f"\n{Colors.red}{Colors.bold}Error: Nothing Selected or user was to dumb to type right{Colors.reset}")
