from functions.tui import tui
from functions.loop import run_checker_loop
import argparse

def main():
    parser = argparse.ArgumentParser(description="Betterer Twitch Notifyer")

    # Argumente hinzufügen
    parser.add_argument('--tui', action='store_true', help="Start the TUI menu")

    args = parser.parse_args()

    if args.tui:
        tui()
    else:
        print("Starting the loop")
        run_checker_loop()

if __name__ == "__main__":
    main()

# to-do:
# Tray?,
# Notification opens Twitch on Click (win10toast, no idea for Linux),
# Options
# Option to remove streamers
# in colors checken ob man CMD benutzt, und den colors befehl nutzten, da windows ein hundesohn ist
