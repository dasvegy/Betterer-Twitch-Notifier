from functions.check_live import check_streamer_live
from functions.colors import Colors
from functions.variables import name_nospace
import os
import json
import sys

user_os = sys.platform

preset = [""]
json_preset = json.dumps(preset, indent=4)


def get_config_path(filename="streamers.json"):
    if sys.platform == "linux":
        config_dir = os.path.join(os.path.expanduser("~"), ".config", name_nospace)
    elif sys.platform == "win32":
        config_dir = os.path.join(os.environ.get("APPDATA", os.path.expanduser("~")), name_nospace)
    elif sys.platform == "darwin":
        config_dir = os.path.join(os.path.expanduser("~"), "Library", "Application Support", name_nospace)
    else:
        raise RuntimeError(f"Unsupported OS: {sys.platform}")

    os.makedirs(config_dir, exist_ok=True)
    file_path = os.path.join(config_dir, filename)

    if not os.path.exists(file_path):
        with open(file_path, "w") as f:
            f.write(json_preset)
        print(f"{file_path} created")

    return file_path


streamers_file_path = get_config_path("streamers.json")


def check_file_no_empty():
    with open(streamers_file_path, "r") as file:
        strmrs_file = json.load(file)

    # Error Handeling
    if (not isinstance(strmrs_file, list) or
            not strmrs_file or
            all(not isinstance(item, str) or
                item.strip() == "" for item in strmrs_file)):
        os.system('cls' if os.name == 'nt' else 'clear')
        input("Error: No Entrys, or no valid entrys \n"
              f"Open the tui menu {Colors.yellow}{Colors.bold}(with -tui){Colors.reset}, then add some Streamers\n\n"
              f"{Colors.red}Press {Colors.bold}Enter {Colors.reset}{Colors.red}to Exit...{Colors.reset}")

        sys.exit(0)


# Loading the streamers from the streamers.json file
def load_streamers(filepath=None):
    if filepath is None:
        filepath = streamers_file_path

    try:
        with open(filepath, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        with open(filepath, "w") as outfile:
            outfile.write(json_preset)
            print(f"{filepath} created, but have not written any streamers in it.")
        return json.loads(json_preset)


def get_usernames():
    for username in load_streamers():
        check_streamer_live(username)
