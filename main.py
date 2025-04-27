import subprocess
import requests
import json
import os
import platform
from plyer import notification

# Get the Username from the User (Temp, replace later)
username = input("What Streamer do you want to search for? \n> ")

# Colors for terminal text / debugging
red = '\033[31m'
green = '\033[32m'
purple = '\033[35m'
white = '\033[0m'


# Check if streamer is live
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
            isonline = False
            print("\n", red, "Streamer Offline\n", white)
        else:
            isonline = True
            print("\n", green, "Streamer Online\n", white)

            send_notification(username, data)

    else:
        print(f"Error")


# Download pfp and save it
def download_pfp(pfp_url, filename=f"pfps/{username}.ico"):
    try:
        img_data = requests.get(pfp_url).content
        with open(filename, 'wb') as handler:
            handler.write(img_data)
        return filename
    except Exception as e:
        print(f"Failed to download pfp: {e}")
        return None


# Send the notification
def send_notification(username, data):
    pfp_url = data[0]["logo"]

    # Check if the Icon already exists
    if os.path.exists(f"pfps/{username}.ico"):
        print("Icon already exists, skipping download")
    else:
        download_pfp(data[0]["logo"])

    # Check platform, bc most Notification daemons on Linux need the absolute path for the Icons
    if platform.system() == "Windows":
        user_icon = f"pfps/{username}.ico"
    elif platform.system() == "Linux":
        user_icon = os.path.abspath(f"pfps/{username}.ico")
    else:
        user_icon = "default.jpg"


    notification.notify(
        title=f"{username} is online!",
        message=f'{data[0]["stream"]["title"]}',
        timeout=3,
        app_icon=user_icon,
    )

# to-do:
# Tray,
# Notification opens Twitch on Click (win10toast, no idea for Linux),
# Automatic Reload,
# Config,
# Type Streamers into a List,
# Options GUI

check_streamer_live(username)
