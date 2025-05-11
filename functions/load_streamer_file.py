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
        with open("streamers.json", "w") as outfile:
            outfile.write(json_preset)
            print("streamers.json created, but have not written any Streamers in it"
                  "\n   (exept me so you know how you have to do it)")
            with open(filepath, "r") as file:
                return json.load(file)


def get_usernames():
    for username in load_streamers():
        check_streamer_live(username)