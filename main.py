from functions.check_live import check_streamer_live
from functions.load_streamer_file import load_streamers

def main():
    for username in load_streamers():
        check_streamer_live(username)

if __name__ == "__main__":
    main()

# to-do:
# Tray?,
# Notification opens Twitch on Click (win10toast, no idea for Linux),
# Automatic Reload,
# Config,
# Type Streamers into a List,
# Options GUI
