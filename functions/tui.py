from functions.load_streamer_file import get_usernames
from functions.add_streamer_file import add_strmrs_to_file
from functions.colors import Colors
import os


def tui():
    os.system('cls' if os.name == 'nt' else 'clear')
    option = input(f"{Colors.purple}{Colors.bold}Betterer Twitch Notifyer{Colors.reset}"
                   "\n------------------------ "
                   "\n1. Check Streamers in the list "
                   "\n2. Add Streamer to the list "
                   "\n3. Change Settings "
                   "\n\nQ: Quit "
                   "\n> ")

    print("")
    if option == "1":
        print("Selected Option 1, Checking for Streamers\n")
        get_usernames()
    elif option == "2":
        print("Selected Option 2, Adding Streamers to list")

        add_strmrs_to_file()
    elif option == "3":
        print("Selected Option 3, loading Settings")
        print(f"{Colors.red}!!! NOT IMPLEMENTED YET !!!{Colors.reset} \nQuitting now...")
        quit()
    elif option == "q" or option == "Q":
        print("Selected Option Q, Exiting...")
        quit()
    else:
        print(f"{Colors.red}{Colors.bold}Error: Nothing Selected or was to dumb to type right{Colors.reset}")
        quit()