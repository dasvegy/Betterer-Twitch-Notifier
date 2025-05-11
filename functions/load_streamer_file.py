from functions.check_live import check_streamer_live
import json


preset = [
    "dasvegy"
]

json_preset = json.dumps(preset, indent=4)

def load_streamers(filepath="streamers.json"):
    try:
        with open(filepath, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        with open(filepath, "w") as outfile:
            outfile.write(json_preset)
            print("streamers.json created, but have not written any streamers in it."
                  "\n(Except for the default one 'dasvegy' to show you the format)")
        return json.loads(json_preset)


def get_usernames():
    for username in load_streamers():
        check_streamer_live(username)