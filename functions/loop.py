from functions.load_streamer_file import get_usernames
import time


# The *loop*
def run_checker_loop(interval_minutes):
    while True:
        get_usernames()
        print(f"Waiting {interval_minutes} minutes...\n")
        time.sleep(interval_minutes * int(60))
