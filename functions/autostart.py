from functions.colors import Colors
import os

user_os = os.name

def autostart_ui():
    # Clear the Terminal
    os.system('cls' if os.name == 'nt' else 'clear')
    if user_os != 'nt':
        autostart_input = input(f"{Colors.orange}{Colors.bold}Autostart Setup{Colors.reset}"
                                f"\n------------------------"
                                f"\n1. Setup via Systemd"
                                f"\n2. I will figure it out"
                                f"\n\n>")

        if autostart_input == "1" or autostart_input == "1.":
            print("Not implemented yet")
        else:
            print("leck eiör")
    elif user_os == 'nt':
        print(os.name)
        print("Windows cumming soon")
    else:
        print("Error")

def check_autostart():
    autostart_ui()