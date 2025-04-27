from functions.check_live import check_streamer_live

# Get the Username from the User
username = input("What Streamer do you want to search for? \n> ")

# to-do:
# Tray,
# Notification opens Twitch on Click (win10toast, no idea for Linux),
# Automatic Reload,
# Config,
# Type Streamers into a List,
# Options GUI

# Function start
if __name__ == "__main__":
    check_streamer_live(username)
