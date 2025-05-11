from functions.load_streamer_file import load_streamers
from functions.colors import Colors
import json
import os

filepath = "streamers.json"

def save_streamers(streamers):
    with open(filepath, "w") as f:
        json.dump(streamers, f, indent=4)

def add_strmrs_to_file(back_callback):
    os.system('cls' if os.name == 'nt' else 'clear')
    strmrs_already_there = load_streamers()
    print(f"Streamers already listed: {Colors.bold}{Colors.purple}{strmrs_already_there}{Colors.reset}\n")

    strmrs_to_add = input("Type streamers to add, separated with a comma \n> ")

    new_strmrs = [s.strip() for s in strmrs_to_add.split(",") if s.strip()]
    combined = strmrs_already_there + [s for s in new_strmrs if s not in strmrs_already_there]

    save_streamers(combined)
    print(f"New Streamerlist: {Colors.bold}{Colors.purple}{combined} {Colors.reset} \n")

    input(f"{Colors.orange}Press {Colors.bold}Enter {Colors.reset}{Colors.orange}to go back...{Colors.reset}")
    back_callback()