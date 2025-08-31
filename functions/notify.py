import os
import platform
from plyer import notification
from functions.download import download_pfp


def send_notification(username, data):
    pfp_path = f"pfps/{username}.ico"

    # Check if the Icon already exists
    if not os.path.exists(pfp_path):
        download_pfp(data[0]["logo"], pfp_path)
    else:
        print("Icon already exists, skipping download.")

    # Set absolute path if necessary
    if platform.system() == "Linux":
        pfp_path = os.path.abspath(pfp_path)
    if platform.system() == "Windows":
        pfp_path = f"pfps/{username}.ico"

    notification.notify(
        title=f"{username} is online!",
        message=f'{data[0]["stream"]["title"]}',
        timeout=3,
        app_icon=pfp_path,
    )
