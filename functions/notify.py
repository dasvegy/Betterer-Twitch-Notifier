from plyer import notification
from functions.download import download_pfp
from functions.variables import name_nospace
import os
import sys
import platform

user_os = sys.platform


def get_pfps_dir(directory="pfps"):
    """

    :rtype: str
    """
    if sys.platform.startswith("linux"):
        config_dir = os.path.join(os.path.expanduser("~"), ".config", name_nospace)
    elif sys.platform == "win32":
        config_dir = os.path.join(os.environ.get("APPDATA", os.path.expanduser("~")), name_nospace)
    elif sys.platform == "darwin":
        config_dir = os.path.join(os.path.expanduser("~"), "Library", "Application Support", name_nospace)
    else:
        raise RuntimeError(f"Unsupported OS: {sys.platform}")

    # create .config / or what folder on what os
    os.makedirs(config_dir, exist_ok=True)

    # create the pfps Folder
    dir_path = os.path.join(config_dir, directory)
    os.makedirs(dir_path, exist_ok=True)

    return dir_path


def send_notification(username, data):
    pfp_dir = get_pfps_dir()
    pfp_path = os.path.join(pfp_dir, f"{username}.ico")

    # Check if the Icon already exists
    if not os.path.exists(pfp_path):
        download_pfp(data[0]["logo"], pfp_path)
    else:
        print("Icon already exists, skipping download.")

    notification.notify(
        title=f"{username} is online!",
        message=f'{data[0]["stream"]["title"]}',
        timeout=3,
        app_icon=pfp_path,
    )
