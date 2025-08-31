from functions.load_streamer_file import get_usernames, check_file_no_empty
from functions.streamer_to_file import add_strmrs_to_file, rm_strmrs_to_file, clear_strmrs_to_file
from functions.settings import settings
from functions.colors import Colors
from functions.variables import name
import os


# The Terminal interface
def tui():
    # Clearing the Terminal
    os.system('cls' if os.name == 'nt' else 'clear')

    # The interface itself
    option = input(f"{Colors.purple}{Colors.bold}{name}{Colors.reset}"
                   "\n------------------------ "
                   "\n1. Check Streamers in the list "
                   "\n2. Add Streamer to the list "
                   "\n3. Remove Streamer to the list "
                   "\n4. Clear Streamerlist "
                   "\n5. Change Settings "
                   "\n\nQ: Quit "
                   "\n> ")
    print("")
    if option == "1":
        print("Selected Option 1, Checking for Streamers\n")
        check_file_no_empty()
        get_usernames()

    elif option == "2":
        print("Selected Option 2, Add Streamers to list")
        add_strmrs_to_file(tui)

    elif option == "3":
        print("Selected Option 3, Remove Streamers to list")
        rm_strmrs_to_file(tui)

    elif option == "4":
        print("Selected Option 4, Clear Streamerlist")
        clear_strmrs_to_file(tui)

    elif option == "5":
        print("Selected Option 5, loading Settings\n")
        settings(tui)

    # Quitting
    elif option == "q" or option == "Q":
        print(f"{Colors.red}{Colors.bold}Exiting...{Colors.reset}")
        quit()

    # Error handeling
    else:
        print(f"{Colors.red}{Colors.bold}Error: Nothing Selected or user was to dumb to type right{Colors.reset}")
        quit()
