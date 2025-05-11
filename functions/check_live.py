from functions.notify import send_notification
from functions.colors import Colors
import requests

def check_streamer_live(username):
    url = f"https://api.ivr.fi/v2/twitch/user?login={username}"
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        print(f"Loading Streamer: {Colors.purple}{Colors.bold}{username}{Colors.reset}")
        print("Successful: code 200")
        data = response.json()

        islive = data[0]["stream"]

        if islive is None:
            print(f"\n{Colors.bold}{Colors.red}Streamer Offline\n{Colors.reset}")
        else:
            print(f"\n{Colors.bold}{Colors.green}Streamer Online\n{Colors.reset}")
            send_notification(username, data)

        print(f"DONE LOADING STREAMER {Colors.purple}{Colors.bold}{username}{Colors.reset}")
        print("---------------------------------------------------------\n")
    else:
        print("Error")