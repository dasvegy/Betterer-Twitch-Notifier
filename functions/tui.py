from functions.load_streamer_file import get_usernames

bold = '\033[01m'
disable = '\033[02m'

purple = '\033[35m'
red = '\033[31m'
white = '\033[0m'


def tui():
    option = input(f"{purple}{bold}Betterer Twitch Notifyer{white}{disable}"
                   "\n------------------------ "
                   "\n1. Check Streamers in the list "
                   "\n2. Add Streamer to the list "
                   "\n3. Change Settings "
                   "\n\nQ: Quit "
                   "\n> ")

    print("")
    if option == "1":
        print("Selected Option 1, Checking for Streamers")
        get_usernames()
    elif option == "2":
        print("Selected Option 2, Adding Streamers to list")
        print(f"{red}!!! NOT IMPLEMENTED YET !!!{white} \nQuitting now...")
        quit()
    elif option == "3":
        print("Selected Option 3, loading Settings")
        print(f"{red}!!! NOT IMPLEMENTED YET !!!{white} \nQuitting now...")
        quit()
    else:
        print("Error: Nothing Selected or was to dumb to type right")
        quit()