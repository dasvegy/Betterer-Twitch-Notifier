import argparse
import sys

from functions.colors import Colors
from functions.config import load_config
from functions.load_streamer_file import check_file_no_empty
from functions.logging import logger
from functions.loop import run_checker_loop
from functions.tray import run_tray
from functions.tui import tui
from functions.variables import name, version_number
from functions.for_windows import attach_or_create_console

logger.info("Starting...")
logger.info(f"Operating System: {sys.platform}")
logger.info(f"Version: {version_number}")
logger.info("vegy is the best")


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
        attach_or_create_console()
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

sys.exit(0)