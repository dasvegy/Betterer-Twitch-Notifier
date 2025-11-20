from functions.tui import tui
from functions.loop import run_checker_loop
from functions.tray import run_tray
from functions.load_streamer_file import check_file_no_empty
from functions.colors import Colors
from functions.variables import name
from functions.config import load_config
import argparse
import asyncio


async def async_main(args, config):
    # launch tray
    if args.tray:
        run_tray()

    print(f"{Colors.bold}{Colors.green}Starting the loop{Colors.reset}\n")
    check_file_no_empty()

    await run_checker_loop(config["interval_minutes"])


def main():
    parser = argparse.ArgumentParser(description=f"{name}")
    parser.add_argument('-tui', action='store_true', help="Start the TUI menu")
    parser.add_argument('-tray', action='store_true', help="Start loop with the Tray")
    args = parser.parse_args()

    if args.tui:
        tui()
        return

    config = load_config()

    # Tray starten (Thread)
    if args.tray:
        run_tray()

    # Checker-Loop synchron starten
    run_checker_loop(config["interval_minutes"])


if __name__ == "__main__":
    main()

quit()

# to-do:
# Autostart !!!
# Tray?,
# Notification öffnet Twitch on Click (win10toast, no idea for Linux),
# Windows (😒) port
