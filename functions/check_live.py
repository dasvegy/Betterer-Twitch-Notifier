from functions.notify import send_notification
from functions.colors import Colors
import requests

strmrs_already_listed = []

class StreamerNotFoundError(Exception):
    def __init__(self, username):
        super().__init__(f"Streamer '{username}' not found or returned no data.")

def check_streamer_live(username):
    url = f"https://api.ivr.fi/v2/twitch/user?login={username}"
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        print(f"Loading Streamer: {Colors.purple}{Colors.bold}{username}{Colors.reset}")
        print("Successful: code 200")
        data = response.json()

        if not data:
            raise StreamerNotFoundError(username)

        islive = data[0]["stream"]

        if islive is None:
            print(f"\n{Colors.bold}{Colors.red}Streamer Offline\n{Colors.reset}")
            if username in strmrs_already_listed:
                strmrs_already_listed.remove(username)
            else:
                pass
        else:
            if username in strmrs_already_listed:
                print("Already send a notification for the Streamer, Next oooooooonne")
                pass
            else:
                print(f"\n{Colors.bold}{Colors.green}Streamer Online\n{Colors.reset}")
                strmrs_already_listed.append(username)
                send_notification(username, data)

        print(f"DONE LOADING STREAMER {Colors.purple}{Colors.bold}{username}{Colors.reset}")
        print("---------------------------------------------------------\n")
    else:
        print(f"Loading Streamer: {Colors.purple}{Colors.bold}{username}{Colors.reset} \n")
        print(f"{Colors.red}Error: API returned status code {response.status_code}{Colors.reset}")

        print(f"\nDONE LOADING STREAMER {Colors.purple}{Colors.bold}{username}{Colors.reset}")
        print("---------------------------------------------------------\n")