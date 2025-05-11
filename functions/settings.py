from functions.colors import Colors
import os

def settings(back_callback):
    os.system('cls' if os.name == 'nt' else 'clear')
    option = input(f"{Colors.purple}{Colors.bold}Betterer Twitch Notifyer{Colors.reset}"
                    "\n------------------------ "
                    f"\n{Colors.yellow}1. placeholder{Colors.reset}"
                    "\n2. Change how often in a hour it should check for online Streamers"
                    "\n\nB: Go Back "
                    "\nQ: Quit "
                    "\n> ")

    if option == "1":
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"{Colors.orange}{Colors.bold}leck eier?{Colors.reset}")
    elif option == "2":
        os.system('cls' if os.name == 'nt' else 'clear')
        # frequency_setting = input(f"{Colors.orange}{Colors.bold}How often in a hour it should check for online Streamers?{Colors.reset}\n\n> ")
        print("Goin back bc its not implemented yet")
        back_callback()
    elif option == "b" or option == "B":
        back_callback()
    elif option == "q" or option == "Q":
        print(f"{Colors.red}{Colors.bold}Exiting...{Colors.reset}")
        quit()
    else:
        print(f"\n{Colors.red}{Colors.bold}Error: Nothing Selected or user was to dumb to type right{Colors.reset}")


