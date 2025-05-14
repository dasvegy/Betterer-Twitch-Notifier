from functions.tui import tui
from functions.loop import run_checker_loop
import argparse
import json

with open("settings.json", "r") as file:
    settings_file = json.load(file)
    interval_minutes = int(settings_file["interval_minutes"])

def main():
    parser = argparse.ArgumentParser(description="Betterer Twitch Notifyer")
    parser.add_argument('--tui', action='store_true', help="Start the TUI menu")
    args = parser.parse_args()

    if args.tui:
        tui()
    else:
        print("Starting the loop")
        run_checker_loop(interval_minutes)

if __name__ == "__main__":
    main()

# to-do:
# Tray?,
# Notification opens Twitch on Click (win10toast, no idea for Linux),
# Windows (😒) port
# in colors checken ob man CMD benutzt, und den colors befehl nutzten, da windows ein hundesohn ist
