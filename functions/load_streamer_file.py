import json

def load_streamers(filepath="streamers.json"):
    try:
        with open(filepath, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
