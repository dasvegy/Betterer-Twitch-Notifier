from functions.check_live import check_streamer_live
from functions.colors import Colors
import os
import json

# A json preset for when there isn't a streamers.json file
preset = [
    ""
]

json_preset = json.dumps(preset, indent=4)

def check_file_no_empty():
    with open("streamers.json", "r") as file:
        strmrs_file = json.load(file)

    # Error Handeling
    if not isinstance(strmrs_file, list):
        os.system('cls' if os.name == 'nt' else 'clear')
        input("Error: No Entrys, or no valid entrys \n"
              f"Open the tui menu {Colors.yellow}{Colors.bold}(with --tui){Colors.reset}, then add some Streamers\n\n"
              f"{Colors.red}Press {Colors.bold}Enter {Colors.reset}{Colors.red}to Exit...{Colors.reset}")

        quit()
    elif not strmrs_file:
        os.system('cls' if os.name == 'nt' else 'clear')
        input("Error: No Entrys, or no valid entrys \n"
              f"Open the tui menu {Colors.yellow}{Colors.bold}(with --tui){Colors.reset}, then add some Streamers\n\n"
              f"{Colors.red}Press {Colors.bold}Enter {Colors.reset}{Colors.red}to Exit...{Colors.reset}")

        quit()
    elif all(not isinstance(item, str) or item.strip() == "" for item in strmrs_file):
        os.system('cls' if os.name == 'nt' else 'clear')
        input("Error: No Entrys, or no valid entrys \n"
              f"Open the tui menu {Colors.yellow}{Colors.bold}(with --tui){Colors.reset}, then add some Streamers\n\n"
              f"{Colors.red}Press {Colors.bold}Enter {Colors.reset}{Colors.red}to Exit...{Colors.reset}")

        quit()
    else:
        pass

# Loading the streamers from the streamers.json file
def load_streamers(filepath="streamers.json"):
    try:
        with open(filepath, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        with open(filepath, "w") as outfile:
            outfile.write(json_preset)
            print("streamers.json created, but have not written any streamers in it.")
        return json.loads(json_preset)

def get_usernames():
    for username in load_streamers():
        check_streamer_live(username)
