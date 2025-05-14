from functions.load_streamer_file import load_streamers
from functions.colors import Colors
import json
import os

# Defines the filepath
filepath = "streamers.json"

# the actual saving part
def save_streamers(streamers):
    with open(filepath, "w") as f:
        json.dump(streamers, f, indent=4)

def check_no_empty_slot():
    with open("streamers.json", "r") as file:
        strmrs_file = json.load(file)

    # removes empty string
    strmrs_file = [s for s in strmrs_file if s.strip() != ""]

    # saves the json file
    with open("streamers.json", "w") as file:
        json.dump(strmrs_file, file, indent=4)

    return strmrs_file

# The Terminal interface (and backend) for saving the Streamer to the streamers.json file
def add_strmrs_to_file(back_callback):
    os.system('cls' if os.name == 'nt' else 'clear')
    check_no_empty_slot()
    strmrs_already_there = load_streamers()
    print(f"Streamers already in the list: {Colors.bold}{Colors.purple}{strmrs_already_there}{Colors.reset}\n")

    strmrs_to_add = input("Type streamers to add, separated with a comma \n> ")

    new_strmrs = [s.strip() for s in strmrs_to_add.split(",") if s.strip()]
    combined = strmrs_already_there + [s for s in new_strmrs if s not in strmrs_already_there]

    save_streamers(combined)
    print(f"New Streamerlist: {Colors.bold}{Colors.purple}{combined} {Colors.reset} \n")

    input(f"{Colors.orange}Press {Colors.bold}Enter {Colors.reset}{Colors.orange}to go back...{Colors.reset}")
    back_callback()

# The Terminal interface (and backend) for removing the Streamer from the streamers.json file
def rm_strmrs_to_file(back_callback):
    os.system('cls' if os.name == 'nt' else 'clear')
    check_no_empty_slot()
    strmrs_already_there = load_streamers()
    print(f"Streamers already in the list: {Colors.bold}{Colors.purple}{strmrs_already_there}{Colors.reset}\n")

    strmrs_to_add = input("Type streamers to remove, separated with a comma \n> ")

    new_strmrs = [s.strip() for s in strmrs_to_add.split(",") if s.strip()]
    combined = [s for s in strmrs_already_there if s not in new_strmrs]

    save_streamers(combined)
    print(f"\nNew Streamerlist: {Colors.bold}{Colors.purple}{combined} {Colors.reset} \n")

    input(f"{Colors.orange}Press {Colors.bold}Enter {Colors.reset}{Colors.orange}to go back...{Colors.reset}")
    back_callback()

# The Terminal interface (and backend) for clearing the streamers.json file
def clear_strmrs_to_file(back_callback):
    os.system('cls' if os.name == 'nt' else 'clear')
    save_streamers([])
    print(f"\nStreamerlist cleared\n")
    input(f"{Colors.orange}Press {Colors.bold}Enter {Colors.reset}{Colors.orange}to go back...{Colors.reset}")
    back_callback()