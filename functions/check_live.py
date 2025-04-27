import requests
import json
from functions.notify import send_notification


# Terminal colors
red = '\033[31m'
green = '\033[32m'
white = '\033[0m'

def check_streamer_live(username):
    url = f"https://api.ivr.fi/v2/twitch/user?login={username}"
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        print("Successful: code 200")
        data = response.json()
        print("JSON OUTPUT: \n\n", json.dumps(data, indent=4), "\n")

        islive = data[0]["stream"]

        if islive is None:
            print(f"\n{red}Streamer Offline\n{white}")
        else:
            print(f"\n{green}Streamer Online\n{white}")
            send_notification(username, data)
    else:
        print("Error")